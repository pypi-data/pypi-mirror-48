import numpy as np
import torch as T
import torch.nn.functional as F
import abc
import threading
import warnings

from queue import Queue
from scipy.stats import truncnorm
from PIL import Image
from slackclient import SlackClient
from torch._six import container_abcs
from itertools import repeat
from functools import wraps, partial, update_wrapper

cuda_available = T.cuda.is_available()


def _wrap(f):
    @wraps(f)
    def wrapper(x, *args, **kwargs):
        return f(x)

    return wrapper


def _make_input_shape(m, n):
    def parse(x):
        if isinstance(x, container_abcs.Iterable):
            return x
        return tuple(repeat(None, m)) + (x, ) + tuple(repeat(None, n))
    return parse


_image_shape = _make_input_shape(1, 2)
_matrix_shape = _make_input_shape(1, 0)
_pointset_shape = _make_input_shape(2, 0)


def validate(func):
    """
    A decorator to make sure output shape is a tuple of ``int`` s.
    """

    def wrapper(self):
        if func(self) is None:
            return None

        out = [None if x is None or np.isnan(x) else int(x) for x in func(self)]
        return tuple(out)

    return wrapper


def no_dim_change_op(cls):
    """
    A decorator to overwrite :attr:`~neuralnet_pytorch.layers._LayerMethod.output_shape`
    to an op that does not change the tensor shape.

    :param cls:
        a subclass of :class:`~neuralnet_pytorch.layers.Module`.
    """

    @validate
    def output_shape(self):
        return None if self.input_shape is None else tuple(self.input_shape)

    cls.output_shape = property(output_shape)
    return cls


def add_simple_repr(cls):
    """
     A decorator to add a simple repr to the designated class.

    :param cls:
        a subclass of :class:`~neuralnet_pytorch.layers.Module`.
     """

    def _repr(self):
        return super(cls, self).__repr__() + ' -> {}'.format(self.output_shape)

    setattr(cls, '__repr__', _repr)
    return cls


def add_custom_repr(cls):
    """
    A decorator to add a custom repr to the designated class.

    :param cls:
        a subclass of :class:`~neuralnet_pytorch.layers.Module`.
    """

    def _repr(self):
        return self.__class__.__name__ + '({}) -> {}'.format(self.extra_repr(), self.output_shape)

    setattr(cls, '__repr__', _repr)
    return cls


def deprecated(new_func, version):
    def _deprecated(func):
        """prints out a deprecation warning"""

        def func_wrapper(*args, **kwargs):
            warnings.warn('%s is deprecated and will be removed in version %s. Use %s instead.' %
                          (func.__name__, version, new_func.__name__), DeprecationWarning)
            return func(*args, **kwargs)

        return func_wrapper
    return _deprecated


def get_non_none(array):
    """
    Gets the first item that is not ``None`` from the given array.

    :param array:
        an arbitrary array that is iterable.
    :return:
        the first item that is not ``None``.
    """

    try:
        e = next(item for item in array if item is not None)
    except StopIteration:
        e = None
    return e


class ThreadsafeIter:
    """
    Takes an iterator/generator and makes it thread-safe by
    serializing call to the `next` method of given iterator/generator.

    Parameters
    ----------
    it
        an iterable object.

    Attributes
    ----------
    lock
        a thread lock.
    """

    def __init__(self, it):
        self.it = it
        self.lock = threading.Lock()

    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            return self.it.__next__()


def threadsafe_generator(generator):
    """
    A decorator that takes a generator function and makes it thread-safe.

    :param generator:
        a generator object.
    :return:
        a thread-safe generator.
    """

    def safe_generator(*agrs, **kwargs):
        return ThreadsafeIter(generator(*agrs, **kwargs))
    return safe_generator


class DataLoader(metaclass=abc.ABCMeta):
    """
    A lightweight data loader. Works comparably to
    Pytorch's :class:`torch.utils.data.Dataloader`
    when the workload is light, but it
    initializes much faster.
    It is totally compatible with :class:`torch.utils.data.Dataset`
    and can be a drop-in for :class:`torch.utils.data.Dataloader`.

    Parameters
    ----------
    dataset
        an instance of :class:`torch.utils.data.Dataset`.
    batch_size
        batch size
    shuffle
        whether to shuffle in each iteration.
    num_workers
        number of threads to be used.
    collate_fn
        function to specify how a batch is loaded.
    augmentation
        an instance of :mod:`torchvision.transforms` classes.
        Applicable to 4D image tensor.
    apply_augmentation_to
        augmentation is only applied to the elements in a batch
        whose indices is specified here.
    num_cached
        number of batches to be cached.
    kwargs
        arguments what will not be used.
        For compatibility with :class:`torch.utils.data.Dataloader` only.

    Attributes
    ----------
    batches
        contains batches of data when iterating over the dataset.
    indices
        contains the indeices of samples of the dataset.
    num_batches
        the number of batches in the dataset.
    """

    def __init__(self, dataset, batch_size, shuffle=False, num_workers=10, collate_fn=None, augmentation=None,
                 apply_augmentation_to=(0,), num_cached=10, **kwargs):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.augmentation = augmentation
        self.num_cached = num_cached
        self.apply_to = apply_augmentation_to
        self.num_workers = num_workers
        self.collate_fn = collate_fn
        self.batches = None
        self.indices = None
        self.num_batches = len(self.dataset) // self.batch_size

    def __iter__(self):
        self.batches = self._get_batches()
        return self

    def __next__(self):
        if self.batches is None:
            self.batches = self._get_batches()
        return self.batches.__next__()

    def _augment_minibatches(self, minibatches):
        for batch in minibatches:
            if isinstance(batch, (list, tuple)):
                assert isinstance(self.apply_to, (list, tuple)), \
                    'Expect a list of indices to which augmentation is applied. Got %s.' % type(self.apply_to)

                for idx in self.apply_to:
                    batch[idx] = [np.transpose(self.augmentation(
                        Image.fromarray((np.transpose(img, (1, 2, 0)) * 255.).astype('uint8'), 'RGB')), (2, 0, 1)) for
                                  img in batch[idx]]
                    batch[idx] = np.stack(batch[idx]).astype('float32') / 255.
            else:
                batch = [np.transpose(self.augmentation(
                        Image.fromarray((np.transpose(img, (1, 2, 0)) * 255.).astype('uint8'), 'RGB')), (2, 0, 1)) for
                                  img in batch]
                batch = np.stack(batch).astype('float32') / 255.
            yield batch.astype

    def _get_batches(self):
        batches = self._generator()
        if self.augmentation:
            batches = self._augment_minibatches(batches)

        batches = self._generate_in_background(batches)
        for it, batch in enumerate(batches):
            batch = T.tensor(batch) if isinstance(batch, np.ndarray) else [T.tensor(b) for b in batch]
            yield batch

    def _generate_in_background(self, generator):
        generator = ThreadsafeIter(generator)
        queue = Queue(maxsize=self.num_cached)

        # define producer (putting items into queue)
        def producer():
            for item in generator:
                queue.put(item)
            queue.join()
            queue.put(None)

        # start producer (in a background thread)
        for i in range(self.num_workers):
            thread = threading.Thread(target=producer, daemon=True)
            thread.start()

        # run as consumer (read items from queue, in current thread)
        while True:
            item = queue.get()
            if item is None:
                break
            yield item
            queue.task_done()

    def _generator(self):
        assert isinstance(self.dataset[0],
                          (list, tuple, np.ndarray)), 'Dataset should consist of lists/tuples or Numpy ndarray'
        self.indices = np.arange(len(self.dataset))
        if self.shuffle:
            np.random.shuffle(self.indices)

        for i in range(self.num_batches):
            slice_ = self.indices[i * self.batch_size:(i + 1) * self.batch_size]
            batch = [self.dataset[s] for s in slice_]

            if isinstance(batch, np.ndarray):
                batch = np.stack(batch, 0)

            if isinstance(batch, (list, tuple)):
                batch = tuple([np.stack(b) for b in zip(*batch)]) if self.collate_fn is None else self.collate_fn(batch)

            yield batch


def truncated_normal(tensor, a=-1, b=1, mean=0., std=1.):
    """
    Initializes a tensor from a truncated normal distribution.

    :param tensor:
        a :class:`torch.Tensor`.
    :param a:
        lower bound of the truncated normal.
    :param b:
        higher bound of the truncated normal.
    :param mean:
        mean of the truncated normal.
    :param std:
        standard deviation of the truncated normal.
    :return:
        ``None``.
    """

    values = truncnorm.rvs(a, b, loc=mean, scale=std, size=list(tensor.shape))
    with T.no_grad():
        tensor.data.copy_(T.tensor(values))


def rgb2gray(img):
    """
    Converts a batch of RGB images to gray.

    :param img:
        an RGB image batch of any type.
    :return:
        a batch of gray images.
    """

    if len(img.shape) != 4:
        raise ValueError('Input images must have four dimensions, not %d' % len(img.shape))

    return (0.299 * img[:, 0] + 0.587 * img[:, 1] + 0.114 * img[:, 2]).unsqueeze(1)


def rgb2ycbcr(img):
    """
    Converts a batch of RGB images to YCbCr.

    :param img:
        an RGB image batch of any type.
    :return:
        a batch of YCbCr images.
    """

    if len(img.shape) != 4:
        raise ValueError('Input images must have four dimensions, not %d' % len(img.shape))

    Y = 0. + .299 * img[:, 0] + .587 * img[:, 1] + .114 * img[:, 2]
    Cb = 128. - .169 * img[:, 0] - .331 * img[:, 1] + .5 * img[:, 2]
    Cr = 128. + .5 * img[:, 0] - .419 * img[:, 1] - .081 * img[:, 2]
    return T.cat((Y.unsqueeze(1), Cb.unsqueeze(1), Cr.unsqueeze(1)), 1)


def ycbcr2rgb(img):
    """
    Converts a batch of YCbCr images to RGB.

    :param img:
        an YCbCr image batch of any type.
    :return:
        a batch of RGB images.
    """

    if len(img.shape) != 4:
        raise ValueError('Input images must have four dimensions, not %d' % len(img.shape))

    R = img[:, 0] + 1.4 * (img[:, 2] - 128.)
    G = img[:, 0] - .343 * (img[:, 1] - 128.) - .711 * (img[:, 2] - 128.)
    B = img[:, 0] + 1.765 * (img[:, 1] - 128.)
    return T.cat((R.unsqueeze(1), G.unsqueeze(1), B.unsqueeze(1)), 1)


def batch_set_value(params, values):
    """
    Sets values of a tensor to another.

    :param params:
        a :class:`torch.Tensor`.
    :param values:
        a :class:`torch.Tensor` of the same shape as `params`.
    :return:
        ``None``.
    """

    for p, v in zip(params, values):
        p.data.copy_(T.from_numpy(v))


def to_numpy(x):
    """
    Moves a tensor to :mod:`numpy`.

    :param x:
        a :class:`torch.Tensor`.
    :return:
        a :class:`numpy.ndarray`.
    """

    return x.cpu().detach().data.numpy()


def to_cuda(x):
    """
    Moves a :mod:`numpy` to tensor.

    :param x:
        a :class:`numpy.ndarray`.
    :return:
        a :class:`torch.Tensor`.
    """

    return T.from_numpy(x).cuda()


def bulk_to_numpy(xs):
    """
    Moves a list of tensors to :class:`numpy.ndarray`.

    :param xs:
        a list/tuple of :class:`torch.Tensor` s.
    :return:
        a tuple of :class:`numpy.ndarray` s.
    """

    return tuple([to_numpy(x) for x in xs])


def bulk_to_cuda(xs):
    """
    Moves a list of :class:`numpy.ndarray` to tensors.

    :param xs:
        a tuple of :class:`numpy.ndarray` s.
    :return:
        a list/tuple of :class:`torch.Tensor` s.
    """

    return tuple([to_cuda(x) for x in xs])


def dimshuffle(x, pattern):
    """
    Reorders the dimensions of this variable, optionally inserting broadcasted dimensions.
    Inspired by `Theano's dimshuffle`_.

    .. _Theano's dimshuffle:
        https://github.com/Theano/Theano/blob/d395439aec5a6ddde8ef5c266fd976412a5c5695/theano/tensor/var.py#L323-L356

    :param x:
        Input tensor.
    :param pattern:
        List/tuple of int mixed with 'x' for broadcastable dimensions.
    :return:
        a tensor whose shape matches `pattern`.

    Examples
    --------
    To create a 3D view of a [2D] matrix, call ``dimshuffle(x, [0,'x',1])``.
    This will create a 3D view such that the
    middle dimension is an implicit broadcasted dimension.  To do the same
    thing on the transpose of that matrix, call ``dimshuffle(x, [1, 'x', 0])``.

    See Also
    --------
    :func:`~neuralnet_pytorch.utils.shape_padleft`
    :func:`~neuralnet_pytorch.utils.shape_padright`
    """

    assert isinstance(pattern, (list, tuple)), 'pattern must be a list/tuple'
    no_expand_pattern = [x for x in pattern if x != 'x']
    y = x.permute(*no_expand_pattern)
    shape = list(y.shape)
    for idx, e in enumerate(pattern):
        if e == 'x':
            shape.insert(idx, 1)
    return y.view(*shape)


def shape_padleft(x, n_ones=1):
    """
    Reshape `x` by left-padding the shape with `n_ones` 1s.
    Inspired by `Theano's shape_padleft`_.

    .. _Theano's shape_padleft:
        https://github.com/Theano/Theano/blob/d395439aec5a6ddde8ef5c266fd976412a5c5695/theano/tensor/basic.py#L4539-L4553

    :param x:
        variable to be reshaped.
    :param n_ones:
        number of 1s to pad.

    See Also
    --------
    :func:`~neuralnet_pytorch.utils.dimshuffle`
    :func:`~neuralnet_pytorch.utils.shape_padright`
    """

    pattern = ('x',) * n_ones + tuple(range(x.ndimension()))
    return dimshuffle(x, pattern)


def shape_padright(x, n_ones=1):
    """
    Reshape `x` by right-padding the shape with `n_ones` 1s.
    Inspired by `Theano's shape_padright`_.

    .. _Theano's shape_padright:
        https://github.com/Theano/Theano/blob/d395439aec5a6ddde8ef5c266fd976412a5c5695/theano/tensor/basic.py#L4557

    :param x:
        variable to be reshaped.
    :param n_ones:
        number of 1s to pad.

    See Also
    --------
    :func:`~neuralnet_pytorch.utils.dimshuffle`
    :func:`~neuralnet_pytorch.utils.shape_padleft`
    """

    pattern = tuple(range(x.ndimension())) + ('x',) * n_ones
    return dimshuffle(x, pattern)


def ravel_index(index, shape):
    """
    Finds the linear index of `index` of a tensor of shape `shape`
    when it is flattened.

    :param index:
        a tuple of ``int`` s.
    :param shape:
        shape of the tensor.
    :return:
        the linear index of the element having `index`.

    Examples
    --------

    >>> import torch as T
    >>> import numpy as np
    >>> import neuralnet_pytorch as nnt
    >>> shape = (2, 3, 5)
    >>> a = T.arange(np.prod(shape)).view(*shape)
    >>> index = (1, 1, 3)
    >>> print(a[index])  # 23
    >>> linear_index = nnt.utils.ravel_index(index, shape)
    >>> print(a.flatten()[linear_index])  # 23
    """

    assert len(index) == len(shape), 'indices and shape must have the same length'
    shape = T.tensor(shape)
    if cuda_available:
        shape = shape.cuda()

    return sum([T.tensor(index[i], dtype=shape.dtype) * T.prod(shape[i + 1:]) for i in range(len(shape))])


def smooth(x, beta=.9, window='hanning'):
    """
    Smooths the data using a window with requested size.
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    :param x:
        the input signal.
    :param beta:
        the weighted moving average coeff. Window length is :math:`1 / (1 - \\beta)`.
    :param window:
        the type of window from ```flat```, ```hanning```, ```hamming```,
        ```bartlett```, and ```blackman```.
        Flat window will produce a moving average smoothing.

    :return:
        the smoothed signal.

    Examples
    --------

    .. code-block:: python

        t = linspace(-2, 2, .1)
        x = sin(t) + randn(len(t)) * .1
        y = smooth(x)

    """

    x = np.array(x)
    assert x.ndim == 1, 'smooth only accepts 1 dimension arrays'
    assert 0 < beta < 1, 'Input vector needs to be bigger than window size'

    window_len = int(1 / (1 - beta))
    if window_len < 3 or x.shape[0] < window_len:
        return x

    s = np.r_[x[window_len - 1:0:-1], x, x[-2:-window_len - 1:-1]]
    if isinstance(window, str):
        assert window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman'], \
            'Window is on of \'flat\', \'hanning\', \'hamming\', \'bartlett\', \'blackman\''

        if window == 'flat':  # moving average
            w = np.ones(window_len, 'd')
        else:
            w = eval('np.' + window + '(window_len)')
    else:
        window = np.array(window)
        assert window.ndim == 1, 'Window must be a 1-dim array'
        w = window

    y = np.convolve(w / w.sum(), s, mode='valid')
    return y if y.shape[0] == x.shape[0] else y[(window_len // 2 - 1):-(window_len // 2)]


def batch_pairwise_dist(x, y):
    bs, num_points_x, points_dim = x.size()
    _, num_points_y, _ = y.size()
    xx = T.bmm(x, x.transpose(2, 1))
    yy = T.bmm(y, y.transpose(2, 1))
    zz = T.bmm(x, y.transpose(2, 1))

    if cuda_available:
        dtype = T.cuda.LongTensor
    else:
        dtype = T.LongTensor

    diag_ind_x = T.arange(0, num_points_x).type(dtype)
    diag_ind_y = T.arange(0, num_points_y).type(dtype)
    # brk()
    rx = xx[:, diag_ind_x, diag_ind_x].unsqueeze(1).expand_as(zz.transpose(2, 1))
    ry = yy[:, diag_ind_y, diag_ind_y].unsqueeze(1).expand_as(zz)
    P = (rx.transpose(2, 1) + ry - 2 * zz)
    return P


def time_cuda_module(f, *args, **kwargs):
    start = T.cuda.Event(enable_timing=True)
    end = T.cuda.Event(enable_timing=True)

    start.record()
    f(*args, **kwargs)
    end.record()

    # Waits for everything to finish running
    T.cuda.synchronize()

    total = start.elapsed_time(end)
    print('Took %fs' % total)
    return total


def slack_message(username, message, channel, token, **kwargs):
    """
    Sends a slack message to the specified chatroom.

    :param username:
        Slack username
    :param message:
        message to be sent.
    :param channel:
        Slack channel.
    :param token:
        Slack chatroom token.
    :param kwargs:
        additional keyword arguments to slack's :meth:`api_call`.
    :return:
        ``None``.
    """

    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel=channel, text=message, username=username, **kwargs)


def relu(x, **kwargs):
    """
    ReLU activation.
    """

    return T.relu(x)


def linear(x, **kwargs):
    """
    Linear activation.
    """

    return x


def lrelu(x, **kwargs):
    """
    Leaky ReLU activation.
    """

    return F.leaky_relu(x, kwargs.get('negative_slope', .2), kwargs.get('inplace', False))


def tanh(x, **kwargs):
    """
    Hyperbolic tangent activation.
    """

    return T.tanh(x)


def sigmoid(x, **kwargs):
    """
    Sigmoid activation.
    """

    return T.sigmoid(x)


def elu(x, **kwargs):
    """
    ELU activation.
    """

    return F.elu(x, kwargs.get('alpha', 1.), kwargs.get('inplace', False))


def softmax(x, **kwargs):
    """
    Softmax activation.
    """

    return T.softmax(x, kwargs.get('dim', None))


def selu(x, **kwargs):
    """
    SELU activation.
    """

    return T.selu(x)


act = {
    'relu': relu,
    'linear': linear,
    None: linear,
    'lrelu': lrelu,
    'tanh': tanh,
    'sigmoid': sigmoid,
    'elu': elu,
    'softmax': softmax,
    'selu': selu
}


def function(activation, **kwargs):
    """
    returns the `activation`.
    Possible choices are
    ``None``, ```linear```, ```relu```, ```lrelu```,
    ```tanh```, ```sigmoid```, ```elu```, ```softmax```,
    and ```selu```.

    :param activation:
        name of the activation function.
    :return:
        activation function
    """

    func = partial(act[activation], **kwargs)
    return update_wrapper(func, act[activation])
