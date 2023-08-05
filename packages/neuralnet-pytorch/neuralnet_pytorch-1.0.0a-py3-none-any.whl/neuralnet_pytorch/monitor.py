from mpl_toolkits.mplot3d import Axes3D
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm

import atexit
import threading
import queue
import numpy as np
import collections
import pickle as pkl
from imageio import imwrite
import os
import time
import visdom
from shutil import copyfile
import torch as T
import torch.nn as nn

try:
    from torch.utils.tensorboard import SummaryWriter
except ImportError:
    from tensorboardX import SummaryWriter

import neuralnet_pytorch as nnt
from neuralnet_pytorch import utils

__all__ = ['Monitor', 'track', 'get_tracked_variables', 'eval_tracked_variables', 'hooks']
_TRACKS = collections.OrderedDict()
hooks = {}


def track(name, x, direction=None):
    """
    An identity function that registers hooks to
    track the value and gradient of the specified tensor.

    Here is an example of how to track an intermediate output ::

        input = ...
        conv1 = nnt.track('op', nnt.Conv2d(shape, 4, 3), 'all')
        conv2 = nnt.Conv2d(conv1.output_shape, 5, 3)
        intermediate = conv1(input)
        output = nnt.track('conv2_output', conv2(intermediate), 'all')
        loss = T.sum(output ** 2)
        loss.backward(retain_graph=True)
        d_inter = T.autograd.grad(loss, intermediate, retain_graph=True)
        d_out = T.autograd.grad(loss, output)
        tracked = nnt.eval_tracked_variables()

        testing.assert_allclose(tracked['conv2_output'], nnt.utils.to_numpy(output))
        testing.assert_allclose(np.stack(tracked['grad_conv2_output']), nnt.utils.to_numpy(d_out[0]))
        testing.assert_allclose(tracked['op'], nnt.utils.to_numpy(intermediate))
        for d_inter_, tracked_d_inter_ in zip(d_inter, tracked['grad_op_output']):
            testing.assert_allclose(tracked_d_inter_, nnt.utils.to_numpy(d_inter_))

    :param name:
        name of the tracked tensor.
    :param x:
        tensor or module to be tracked.
        If module, the output of the module will be tracked.
    :param direction:
        there are 4 options

        ``None``: tracks only value.

        ```forward```: tracks only value.

        ```backward```: tracks only gradient.

        ```all``: tracks both value and gradient.

        Default: ``None``.
    :return: `x`.
    """

    assert isinstance(name, str), 'name must be a string, got %s' % type(name)
    assert isinstance(x, (T.nn.Module, T.Tensor)), 'x must be a Torch Module or Tensor, got %s' % type(x)
    assert direction in (
        'forward', 'backward', 'all', None), 'direction must be None, \'forward\', \'backward\', or \'all\''

    if isinstance(x, T.nn.Module):
        if direction in ('forward', 'all', None):
            def _forward_hook(module, input, output):
                _TRACKS[name] = output.detach()

            hooks[name] = x.register_forward_hook(_forward_hook)

        if direction in ('backward', 'all'):
            def _backward_hook(module, grad_input, grad_output):
                _TRACKS['grad_' + name + '_output'] = tuple([grad_out.detach() for grad_out in grad_output])

            hooks['grad_' + name + '_output'] = x.register_backward_hook(_backward_hook)
    else:
        if direction in ('forward', 'all', None):
            _TRACKS[name] = x.detach()

        if direction in ('backward', 'all'):
            def _hook(grad):
                _TRACKS['grad_' + name] = tuple([grad_.detach() for grad_ in grad])

            hooks['grad_' + name] = x.register_hook(_hook)

    return x


def get_tracked_variables(name=None, return_name=False):
    """
    Gets tracked variable given name.

    :param name:
        name of the tracked variable.
        can be ``str`` or``list``/``tuple`` of ``str``s.
        If ``None``, all the tracked variables will be returned.
    :param return_name:
        whether to return the names of the tracked variables.
    :return:
        the tracked variables.
    """

    assert isinstance(name, (str, list, tuple)) or name is None, 'name must either be None, a tring, or a list/tuple.'
    if name is None:
        tracked = ([n for n in _TRACKS.keys()], [val for val in _TRACKS.values()]) if return_name \
            else [val for val in _TRACKS.values()]
        return tracked
    elif isinstance(name, (list, tuple)):
        tracked = (name, [_TRACKS[n] for n in name]) if return_name else [_TRACKS[n] for n in name]
        return tracked
    else:
        tracked = (name, _TRACKS[name]) if return_name else _TRACKS[name]
        return tracked


def eval_tracked_variables():
    """
    Retrieves the values of tracked variables.

    :return: a dictionary containing the values of tracked variables
        associated with the given names.
    """

    name, vars = get_tracked_variables(return_name=True)
    dict = collections.OrderedDict()
    for n, v in zip(name, vars):
        if isinstance(v, (list, tuple)):
            dict[n] = [val.item() if val.numel() == 1 else utils.to_numpy(val) for val in v]
        else:
            dict[n] = v.item() if v.numel() == 1 else utils.to_numpy(v)
    return dict


def _spawn_defaultdict_ordereddict():
    return collections.OrderedDict()


class Monitor:
    """
    Collects statistics and displays the results using various backends.
    The collected stats are stored in '<root>/<model_name>/run<#id>'
    where #id is automatically assigned each time a new run starts.

    Examples
    --------
    The following snippet shows how to collect statistics and display them
    every 100 iterations.

    .. code-block:: python

        import neuralnet as nnt

        ...
        mon = nnt.Monitor(model_name='my_model', print_freq=100)
        for epoch in n_epochs:
            for data in data_loader:
                with mon:
                    loss = net(data)
                    mon.plot('training loss', loss)
                    mon.imwrite('input images', data['images'])
        ...

    Parameters
    ----------
    model_name : str
        name of the model folder.
    root : str
        path to store the collected statistics.
    current_folder : str
        if given, all the stats in here will be overwritten or resumed.
    print_freq : int
        statistics display frequency. Used only in context manager mode.
    num_iters : int
        number of iterations/epoch.
        If specified, training iteration percentage will be displayed along with epoch.
    use_visdom : bool
        whether to use Visdom for real-time monitoring.
    use_tensorboard : bool
        whether to use Tensorboard for real-time monitoring.
    send_slack : bool
        whether to send the statistics to Slack chatroom.
    kwargs
        some miscellaneous options for Visdom and other functions.

    Attributes
    ----------
    path
        contains all the runs of `model_name`.
    current_folder
        path to the current run.
    vis
        an instance of :mod:`Visdom` when `~use_visdom` is set to ``True``.
    writer
        an instance of Tensorboard's :class:`SummaryWriter`
        when `~use_tensorboard` is set to ``True``.
    """

    def __init__(self, model_name='my_model', root='results', current_folder=None, print_freq=None, num_iters=None,
                 use_visdom=False, use_tensorboard=False, send_slack=False, **kwargs):
        self._iter = 0
        self._num_since_beginning = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._num_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._img_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._hist_since_beginning = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._hist_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._pointcloud_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._options = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._dump_files = collections.OrderedDict()
        self._schedule = {'beginning': collections.defaultdict(_spawn_defaultdict_ordereddict),
                          'end': collections.defaultdict(_spawn_defaultdict_ordereddict)}
        self._timer = time.time()
        self._io_method = {'pickle_save': self._save_pickle, 'txt_save': self._save_txt,
                           'torch_save': self._save_torch, 'pickle_load': self._load_pickle,
                           'txt_load': self._load_txt, 'torch_load': self._load_torch}

        self._last_epoch = 0
        self.print_freq = print_freq
        if current_folder:
            self.current_folder = current_folder
            try:
                log = self.read_log('log.pkl')
                try:
                    self._set_num_stats(log['num'])
                except KeyError:
                    print('No record found for \'num\'')

                try:
                    self._set_hist_stats(log['hist'])
                except KeyError:
                    print('No record found for \'hist\'')

                try:
                    self._set_options(log['options'])
                except KeyError:
                    print('No record found for \'options\'')

                try:
                    self.set_iter(log['iter'])
                except KeyError:
                    print('No record found for \'iter\'')

                try:
                    self._last_epoch = log['epoch']
                except KeyError:
                    print('No record found for \'epoch\'')

            except FileNotFoundError:
                print('\'log.pkl\' not found in \'%s\'' % self.current_folder)

        else:
            self.path = os.path.join(root, model_name)
            os.makedirs(self.path, exist_ok=True)
            subfolders = os.listdir(self.path)
            self.current_folder = os.path.join(self.path, 'run%d' % (len(subfolders) + 1))
            idx = 1
            while os.path.exists(self.current_folder):
                self.current_folder = os.path.join(self.path, 'run%d' % (len(subfolders) + 1 + idx))
                idx += 1
            os.makedirs(self.current_folder, exist_ok=True)

        self.use_visdom = use_visdom
        if use_visdom:
            if kwargs.pop('disable_visdom_logging', True):
                import logging
                logging.disable(logging.CRITICAL)

            server = kwargs.pop('server', 'http://localhost')
            port = kwargs.pop('port', 8097)
            self.vis = visdom.Visdom(server=server, port=port)
            if not self.vis.check_connection():
                from subprocess import Popen, PIPE
                Popen('visdom', stdout=PIPE, stderr=PIPE)

            self.vis.close()
            print('You can navigate to \'%s:%d\' for visualization' % (server, port))

        self.use_tensorboard = use_tensorboard
        if use_tensorboard:
            os.makedirs(os.path.join(self.current_folder, 'tensorboard'), exist_ok=True)
            self.writer = SummaryWriter(os.path.join(self.current_folder, 'tensorboard'))

        self._q = queue.Queue()
        self._thread = threading.Thread(target=self._work, daemon=True)
        self._thread.start()

        self.num_iters = num_iters

        self.send_slack = send_slack
        if send_slack:
            assert kwargs.get('channel', None) is not None and kwargs.get('token', None) is not None, \
                'channel and token must be provided to send a slack message'

            if kwargs.get('username', None) is None:
                kwargs['username'] = 'me'

        self.kwargs = kwargs

        atexit.register(self._atexit)
        print('Result folder: %s' % self.current_folder)

    @property
    def iter(self):
        """
        returns the current iteration.

        :return: :attr:`~_iter`.
        """

        return self._iter

    def set_iter(self, iter_num):
        """
        sets the iteration counter to a specific value.

        :param iter_num:
            the iteration number to set.
        :return: ``None``.
        """

        self._iter = iter_num

    def _set_num_stats(self, stats_dict):
        self._num_since_beginning.update(stats_dict)

    def _set_hist_stats(self, stats_dict):
        self._hist_since_beginning.update(stats_dict)

    def _set_options(self, options_dict):
        self._options.update(options_dict)

    def set_option(self, name, option, value):
        """
        sets option for histogram plotting.

        :param name:
             name of the histogram plot.
             Must be the same as the one specified when using :meth:`~hist`.
        :param option:
            there are two options which should be passed as a ``str``.

            ```last_only```: plot the histogram of the last recorded tensor only.

            ```n_bins```: number of bins of the histogram.
        :param value:
            value of the chosen option. Should be ``True``/``False`` for ```last_only```
            and an integer for ```n_bins```.
        :return: ``None``.
        """

        self._options[name][option] = value

    def clear_scalar_stats(self, key):
        """
        removes the collected statistics for scalar plot of the specified `key`.

        :param key:
            the name of the scalar collection.
        :return: ``None``.
        """

        self._num_since_beginning[key].clear()

    def clear_hist_stats(self, key):
        """
        removes the collected statistics for histogram plot of the specified `key`.

        :param key:
            the name of the histogram collection.
        :return: ``None``.
        """

        self._hist_since_beginning[key].clear()

    def get_epoch(self):
        """
        returns the current epoch.
        """
        return self._last_epoch

    def run_training(self, net, train_loader, n_epochs, eval_loader=None, valid_freq=None, start_epoch=None,
                     train_stats_func=None, val_stats_func=None, *args, **kwargs):
        """
        runs the training loop for the given neural network.

        Examples
        --------

        .. code-block:: python

            import neuralnet_pytorch as nnt

            class MyNet(nnt.Net, nnt.Module):
                ...

            # define the network, and training and testing loaders
            net = MyNet(...)
            train_loader = ...
            eval_loader = ...

            # instantiate a Monitor object
            mon = Monitor(model_name='my_net', print_freq=100)

            # save string representations of the model, optimization and lr scheduler
            mon.dump_model(net)
            mon.dump_rep('optimizer', net.optim['optimizer'])
            if net.optim['scheduler']:
                mon.dump_rep('scheduler', net.optim['scheduler'])

            # collect the parameters of the network
            states = {
                'model_state_dict': net.state_dict(),
                'opt_state_dict': net.optim['optimizer'].state_dict()
            }
            if net.optim['scheduler']:
                states['scheduler_state_dict'] = net.optim['scheduler'].state_dict()

            # save a checkpoint after each epoch and keep only the 5 latest checkpoints
            mon.schedule(mon.dump, beginning=False, name='training.pt', obj=states, type='torch', keep=5)

            print('Training...')

            # run the training loop
            mon.run_training(net, train_loader, n_epochs, eval_loader, valid_freq=val_freq)
            print('Training finished!')

        :param net:
            must be an instance of :class:`~neuralnet_pytorch.layers.Net`
            and :class:`~neuralnet_pytorch.layers.Module`.
        :param train_loader:
            provides training data for neural net.
        :param n_epochs:
            number of training epochs.
        :param eval_loader:
            provides validation data for neural net. Optional.
        :param valid_freq:
            indicates how often validation is run.
            In effect if only `eval_loader` is given.
        :param start_epoch:
            the epoch from which training will continue.
            If ``None``, training counter will be set to 0.
        :param train_stats_func:
            a custom function to handle statistics returned from the training procedure.
            If ``None``, a default handler will be used.
            For a list of suported statistics, see :class:`~neuralnet_pytorch.layers.Net`.
        :param val_stats_func:
            a custom function to handle statistics returned from the validation procedure.
            If ``None``, a default handler will be used.
            For a list of suported statistics, see :class:`~neuralnet_pytorch.layers.Net`.
        :param args:
            additional arguments that will be passed to neural net.
        :param kwargs:
            additional keyword arguments that will be passed to neural net.
        :return: ``None``.
        """

        assert isinstance(net, nnt.Net), 'net must be an instance of Net'
        assert isinstance(net, (nnt.Module, nn.Module, nnt.Sequential, nn.Sequential)), \
            'net must be an instance of Module or Sequential'

        collect = {
            'scalars': self.plot,
            'images': self.imwrite,
            'histograms': self.hist,
            'pointclouds': self.scatter
        }

        start_epoch = self._last_epoch if start_epoch is None else start_epoch
        for epoch in range(start_epoch, n_epochs):
            self._last_epoch = epoch
            if net.optim['scheduler'] is not None:
                net.optim['scheduler'].step(epoch)

            for func_dict in self._schedule['beginning'].values():
                func_dict['func'](*func_dict['args'], **func_dict['kwargs'])

            for it, batch in enumerate(train_loader):
                net.train(True)
                with self:
                    batch_cuda = list(batch)
                    if nnt.cuda_available:
                        for i in range(len(batch_cuda)):
                            if not isinstance(batch_cuda[i], (list, tuple)):
                                batch_cuda[i] = batch_cuda[i].cuda()
                            else:
                                batch_cuda[i] = list(batch_cuda[i])
                                for ii in range(len(batch_cuda[i])):
                                    batch_cuda[i][ii] = batch_cuda[i][ii].cuda()

                    net.learn(*batch_cuda, *args, **kwargs)

                    if train_stats_func is None:
                        for t, d in net.stats['train'].items():
                            for k, v in d.items():
                                if t == 'scalars':
                                    if np.isnan(v) or np.isinf(v):
                                        raise ValueError('{} is NaN/inf. Training failed!'.format(k))

                                collect[t](k, v)
                    else:
                        train_stats_func(net.stats['train'])

                    if valid_freq:
                        if it % valid_freq == 0:
                            net.eval()

                            with T.set_grad_enabled(False):
                                eval_dict = {
                                    'scalars': collections.defaultdict(lambda: []),
                                    'histograms': collections.defaultdict(lambda: [])
                                }

                                for itt, batch in enumerate(eval_loader):
                                    batch_cuda = list(batch)
                                    if nnt.cuda_available:
                                        for i in range(len(batch_cuda)):
                                            if not isinstance(batch_cuda[i], (list, tuple)):
                                                batch_cuda[i] = batch_cuda[i].cuda()
                                            else:
                                                batch_cuda[i] = list(batch_cuda[i])
                                                for ii in range(len(batch_cuda[i])):
                                                    batch_cuda[i][ii] = batch_cuda[i][ii].cuda()

                                    try:
                                        net.eval_procedure(*batch_cuda, *args, **kwargs)
                                    except NotImplementedError:
                                        print('An evaluation procedure must be specified')
                                        raise

                                    if val_stats_func is None:
                                        for t, d in net.stats['eval'].items():
                                            if t in ('scalars', 'histograms'):
                                                for k, v in d.items():
                                                    eval_dict[t][k].append(v)
                                            else:
                                                for k, v in d.items():
                                                    collect[t](k, v)
                                    else:
                                        val_stats_func(net.stats['eval'])

                                for t in ('scalars', 'histograms'):
                                    for k, v in eval_dict[t].items():
                                        v = np.mean(v) if t == 'scalars' else np.concatenate(v)
                                        collect[t](k, v)

            for func_dict in self._schedule['end'].values():
                func_dict['func'](*func_dict['args'], **func_dict['kwargs'])

    def _atexit(self):
        self.flush()
        plt.close()
        if self.use_tensorboard:
            self.writer.close()

        self._q.join()

    def dump_rep(self, name, obj):
        """
        saves a string representation of the given object.

        :param name:
            name of the txt file containing the string representation.
        :param obj:
            object to saved as string representation.
        :return: ``None``.
        """

        with open(os.path.join(self.current_folder, name + '.txt'), 'w') as outfile:
            outfile.write(str(obj))
            outfile.close()

    def dump_model(self, network, *args, **kwargs):
        """
        saves a string representation of the given neural net.

        :param network:
            neural net to be saved as string representation.
        :param args:
            additional arguments to Tensorboard's :meth:`SummaryWriter`
            when :attr:`~use_tensorboard` is ``True``.
        :param kwargs:
            additional keyword arguments to Tensorboard's :meth:`SummaryWriter`
            when :attr:`~use_tensorboard` is ``True``.
        :return: ``None``.
        """

        assert isinstance(network, (
            nn.Module, nn.Sequential)), 'network must be an instance of Module or Sequential, got {}'.format(
            type(network))
        self.dump_rep('network.txt', network)
        if self.use_tensorboard:
            self.writer.add_graph(network, *args, **kwargs)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.print_freq:
            if self._iter % self.print_freq == 0:
                self.flush()
        self.tick()

    def copy_file(self, file):
        """
        saves a copy of the given file to :attr:`~current_folder`.

        :param file:
            file to be saved.
        :return: ``None``.
        """

        copyfile(file, '%s/%s' % (self.current_folder, os.path.split(file)[1]))

    def tick(self):
        """
        increases the iteration counter by 1.
        Do not call this if using :class:`Monitor`'s context manager mode.

        :return: ``None``.
        """
        self._iter += 1

    def plot(self, name: str, value):
        """
        schedules a plot of scalar value.
        A :mod:`matplotlib` figure will be rendered and saved every :attr:`~print_freq` iterations.

        :param name:
            name of the figure to be saved. Must be unique among plots.
        :param value:
            scalar value to be plotted.
        :return: ``None``.
        """

        if isinstance(value, T.Tensor):
            value = utils.to_numpy(value)

        self._num_since_last_flush[name][self._iter] = value
        if self.use_tensorboard:
            self.writer.add_scalar('data/' + name.replace(' ', '-'), value, self._iter)

    def scatter(self, name, value):
        """
        schedules a scattor plot of (a batch of) points.
        A 3D :mod:`matplotlib` figure will be rendered and saved every :attr:`~print_freq` iterations.

        :param name:
            name of the figure to be saved. Must be unique among plots.
        :param value:
            2D or 3D tensor to be plotted. The last dim should be 3.
        :return: ``None``.
        """

        if isinstance(value, T.Tensor):
            value = utils.to_numpy(value)

        self._pointcloud_since_last_flush[name][self._iter] = value

    def imwrite(self, name: str, value):
        """
        schedules to save images.
        The images will be rendered and saved every :attr:`~print_freq` iterations.

        :param name:
            name of the figure to be saved. Must be unique among plots.
        :param value:
            3D or 4D tensor to be plotted.
            The expected shape is (C, H, W) for 3D tensors and
            (N, C, H, W) for 4D tensors.
            If the number of channels is other than 3 or 1, each channel is saved as
            a gray image.
        :return: ``None``.
        """

        if isinstance(value, T.Tensor):
            value = utils.to_numpy(value)

        self._img_since_last_flush[name][self._iter] = value
        if self.use_tensorboard:
            self.writer.add_image('image/' + name.replace(' ', '-'), value, self._iter)

    @utils.deprecated(imwrite, '0.0.6')
    def save_image(self, name: str, value):
        """
        schedules to save images.
        Deprecated in favor of :meth:`~imwrite`.
        """

        self.imwrite(name, value)

    def hist(self, name, value, n_bins=20, last_only=False):
        """
        schedules a histogram plot of (a batch of) points.
        A :mod:`matplotlib` figure will be rendered and saved every :attr:`~print_freq` iterations.

        :param name:
            name of the figure to be saved. Must be unique among plots.
        :param value:
            any-dim tensor to be histogrammed. The last dim should be 3.
        :return: ``None``.
        """

        if isinstance(value, T.Tensor):
            value = utils.to_numpy(value)

        if self._iter == 0:
            self._options[name]['last_only'] = last_only
            self._options[name]['n_bins'] = n_bins

        self._hist_since_last_flush[name][self._iter] = value
        if self.use_tensorboard:
            self.writer.add_histogram('hist/' + name.replace(' ', '-'), value, self._iter)

    def schedule(self, func, beginning=True, *args, **kwargs):
        """
        uses to schedule a routine during every epoch in :meth:`~run_training`.

        :param func:
            a routine to be executed in :meth:`~run_training`.
        :param beginning:
            whether to run at the beginning of every epoch. Default: ``True``.
        :param args:
            additional arguments to `func`.
        :param kwargs:
            additional keyword arguments to `func`.
        :return: ``None``
        """

        assert callable(func), 'func must be callable'
        name = func.__name__
        when = 'beginning' if beginning else 'end'
        self._schedule[when][name]['func'] = func
        self._schedule[when][name]['args'] = args
        self._schedule[when][name]['kwargs'] = kwargs

    def _worker(self, it, _num_since_last_flush, _img_since_last_flush, _hist_since_last_flush,
                _pointcloud_since_last_flush):
        prints = []

        # plot statistics
        fig = plt.figure()
        plt.xlabel('iteration')
        for name, vals in list(_num_since_last_flush.items()):
            self._num_since_beginning[name].update(vals)

            x_vals = list(self._num_since_beginning[name].keys())
            plt.ylabel(name)
            y_vals = [self._num_since_beginning[name][x] for x in x_vals]
            if isinstance(y_vals[0], dict):
                keys = list(y_vals[0].keys())
                y_vals = [tuple([y_val[k] for k in keys]) for y_val in y_vals]
                plot = plt.plot(x_vals, y_vals)
                plt.legend(plot, keys)
                prints.append(
                    "{}\t{:.5f}".format(name,
                                        np.mean(np.array([[val[k] for k in keys] for val in vals.values()]), 0)))
            else:
                max_, min_, med_, mean_ = np.max(y_vals), np.min(y_vals), np.median(y_vals), np.mean(y_vals)
                argmax_, argmin_ = np.argmax(y_vals), np.argmin(y_vals)
                plt.title('max: {:.8f} at iter {} \nmin: {:.8f} at iter {} \nmedian: {:.8f} '
                          '\nmean: {:.8f}'.format(max_, x_vals[argmax_], min_, x_vals[argmin_], med_, mean_))

                plt.plot(x_vals, y_vals)
                prints.append("{}\t{:.6f}".format(name, np.mean(np.array(list(vals.values())), 0)))

            fig.savefig(os.path.join(self.current_folder, name.replace(' ', '_') + '.jpg'))
            if self.use_visdom:
                self.vis.matplot(fig, win=name)
            fig.clear()

        # save recorded images
        for name, vals in list(_img_since_last_flush.items()):
            for val in vals.values():
                if val.dtype != 'uint8':
                    val = (255.99 * val).astype('uint8')
                if len(val.shape) == 4:
                    if self.use_visdom:
                        self.vis.images(val, win=name)
                    for num in range(val.shape[0]):
                        img = val[num]
                        if img.shape[0] == 3:
                            img = np.transpose(img, (1, 2, 0))
                            imwrite(os.path.join(self.current_folder, name.replace(' ', '_') + '_%d.jpg' % num),
                                    img)
                        else:
                            for ch in range(img.shape[0]):
                                img_normed = (img[ch] - np.min(img[ch])) / (np.max(img[ch]) - np.min(img[ch]))
                                imwrite(os.path.join(self.current_folder,
                                                     name.replace(' ', '_') + '_%d_%d.jpg' % (num, ch)), img_normed)
                elif len(val.shape) == 3 or len(val.shape) == 2:
                    if self.use_visdom:
                        self.vis.image(val if len(val.shape) == 2 else np.transpose(val, (2, 0, 1)), win=name)
                    imwrite(os.path.join(self.current_folder, name.replace(' ', '_') + '.jpg'), val)
                else:
                    raise NotImplementedError

        # make histograms of recorded data
        for name, vals in list(_hist_since_last_flush.items()):
            if self.use_tensorboard:
                k = max(list(_hist_since_last_flush[name].keys()))
                val = np.array(vals[k]).flatten()
                self.writer.add_histogram(name, val, global_step=k)

            n_bins = self._options[name].get('n_bins')
            last_only = self._options[name].get('last_only')

            if last_only:
                k = max(list(_hist_since_last_flush[name].keys()))
                val = np.array(vals[k]).flatten()
                plt.hist(val, bins='auto')
            else:
                self._hist_since_beginning[name].update(vals)

                z_vals = list(self._hist_since_beginning[name].keys())
                vals = [np.array(self._hist_since_beginning[name][i]).flatten() for i in z_vals]
                hists = [np.histogram(val, bins=n_bins) for val in vals]
                y_vals = np.array([hists[i][0] for i in range(len(hists))])
                x_vals = np.array([hists[i][1] for i in range(len(hists))])
                x_vals = (x_vals[:, :-1] + x_vals[:, 1:]) / 2.
                z_vals = np.tile(z_vals[:, None], (1, n_bins))

                ax = fig.gca(projection='3d')
                surf = ax.plot_surface(x_vals, z_vals, y_vals, cmap=cm.coolwarm, linewidth=0, antialiased=False)
                ax.view_init(45, -90)
                fig.colorbar(surf, shrink=0.5, aspect=5)
            fig.savefig(os.path.join(self.current_folder, name.replace(' ', '_') + '_hist.jpg'))
            fig.clear()

        # scatter pointcloud(s)
        for name, vals in list(_pointcloud_since_last_flush.items()):
            vals = list(vals.values())[-1]
            if len(vals.shape) == 2:
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(*[vals[:, i] for i in range(vals.shape[-1])])
                plt.savefig(os.path.join(self.current_folder, name.replace(' ', '_') + '.jpg'))
            elif len(vals.shape) == 3:
                for ii in range(vals.shape[0]):
                    ax = fig.add_subplot(111, projection='3d')
                    ax.scatter(*[vals[ii, :, i] for i in range(vals.shape[-1])])
                    plt.savefig(os.path.join(self.current_folder, name.replace(' ', '_') + '_%d.jpg' % (ii + 1)))
                    fig.clear()
        plt.close('all')

        with open(os.path.join(self.current_folder, 'log.pkl'), 'wb') as f:
            pkl.dump({'iter': it, 'epoch': self._last_epoch,
                      'num': dict(self._num_since_beginning),
                      'hist': dict(self._hist_since_beginning),
                      'options': dict(self._options)}, f, pkl.HIGHEST_PROTOCOL)

        iter_show = 'Iteration {}/{} ({:.2f}%) Epoch {}'.format(it % self.num_iters, self.num_iters,
                                                                (it % self.num_iters) / self.num_iters * 100.,
                                                                it // self.num_iters + 1) if self.num_iters \
            else 'Iteration {}'.format(it)
        log = 'Elapsed time {:.2f}min\t{}\t{}'.format((time.time() - self._timer) / 60., iter_show,
                                                      '\t'.join(prints))
        print(log)

        if self.send_slack:
            message = 'From %s ' % self.current_folder
            message += log
            utils.slack_message(message=message, **self.kwargs)

    def _work(self):
        while True:
            items = self._q.get()
            work = items[0]
            work(*items[1:])
            self._q.task_done()

    def flush(self):
        """
        executes all the scheduled plots.
        Do not call this if using :class:`Monitor`'s context manager mode.

        :return: ``None``.
        """

        self._q.put((self._worker, self._iter, dict(self._num_since_last_flush), dict(self._img_since_last_flush),
                     dict(self._hist_since_last_flush), dict(self._pointcloud_since_last_flush)))
        self._num_since_last_flush.clear()
        self._img_since_last_flush.clear()
        self._hist_since_last_flush.clear()
        self._pointcloud_since_last_flush.clear()

    def _version(self, file, keep):
        name, ext = os.path.splitext(file)
        versioned_filename = os.path.normpath(name + '-%d' % self._iter + ext)

        if file not in self._dump_files.keys():
            self._dump_files[file] = []

        if versioned_filename not in self._dump_files[file]:
            self._dump_files[file].append(versioned_filename)

        if len(self._dump_files[file]) > keep:
            oldest_file = self._dump_files[file][0]
            full_file = os.path.join(self.current_folder, oldest_file)
            if os.path.exists(full_file):
                os.remove(full_file)
            else:
                print("The oldest saved file does not exist")
            self._dump_files[file].remove(oldest_file)

        with open(os.path.join(self.current_folder, '_version.pkl'), 'wb') as f:
            pkl.dump(self._dump_files, f, pkl.HIGHEST_PROTOCOL)
        return versioned_filename

    def dump(self, name, obj, type='pickle', keep=-1, **kwargs):
        """
        saves the given object.

        :param name:
            name of the file to be saved.
        :param obj:
            object to be saved.
        :param type:
            there are 3 types of data format.

            ```pickle```: use :func:`pickle.dump` to store object.

            ```torch```: use :func:`torch.save` to store object.

            ```txt```: use :func:`numpy.savetxt` to store object.

            Default: ```pickle```.
        :param keep:
            the number of versions of the saved file to keep.
            Default: -1 (keeps only the latest version).
        :param kwargs:
            additional keyword arguments to the underlying save function.
        :return: ``None``.
        """

        self._dump(name.replace(' ', '_'), obj, keep, self._io_method[type + '_save'], **kwargs)

    def load(self, file, type='pickle', version=-1, **kwargs):
        """
        loads from the given file.

        :param file:
            name of the saved file without version.
        :param type:
            there are 3 types of data format.

            ```pickle```: use :func:`pickle.load` to store object.

            ```torch```: use :func:`torch.load` to store object.

            ```txt```: use :func:`numpy.loadtxt` to store object.

            Default: ```pickle```.
        :param version:
            the version of the saved file to load.
            Default: -1 (loads the latest version of the saved file).
        :param kwargs:
            additional keyword arguments to the underlying load function.
        :return: ``None``.
        """

        return self._load(file, self._io_method[type + '_load'], version, **kwargs)

    def _dump(self, name, obj, keep, method, **kwargs):
        """Should not be called directly."""
        assert isinstance(keep, int), 'keep must be an int, got %s' % type(keep)

        if keep < 2:
            name = os.path.join(self.current_folder, name)
            method(name, obj, **kwargs)
            print('Object dumped to %s' % name)
        else:
            normed_name = self._version(name, keep)
            normed_name = os.path.join(self.current_folder, normed_name)
            method(normed_name, obj, **kwargs)
            print('Object dumped to %s' % normed_name)

    def _load(self, file, method, version=-1, **kwargs):
        """Should not be called directly."""
        assert isinstance(version, int), 'keep must be an int, got %s' % type(version)

        full_file = os.path.join(self.current_folder, file)
        try:
            with open(os.path.join(self.current_folder, '_version.pkl'), 'rb') as f:
                self._dump_files = pkl.load(f)

            versions = self._dump_files.get(file, [])
            if len(versions) == 0:
                try:
                    obj = method(full_file, **kwargs)
                except FileNotFoundError:
                    print('No file named %s found' % file)
                    return None
            else:
                if version <= 0:
                    if len(versions) > 0:
                        latest = versions[-1]
                        obj = method(os.path.join(self.current_folder, latest), **kwargs)
                    else:
                        return method(full_file, **kwargs)
                else:
                    name, ext = os.path.splitext(file)
                    file_name = os.path.normpath(name + '-%d' % version + ext)
                    if file_name in versions:
                        obj = method(os.path.join(self.current_folder, file_name), **kwargs)
                    else:
                        print('Version %d of %s is not found in %s' % (version, file, self.current_folder))
                        return None
        except FileNotFoundError:
            try:
                obj = method(full_file, **kwargs)
            except FileNotFoundError:
                print('No file named %s found' % file)
                return None

        text = str(version) if version > 0 else 'latest'
        print('Version \'%s\' loaded' % text)
        return obj

    def _save_pickle(self, name, obj):
        with open(name, 'wb') as f:
            pkl.dump(obj, f, pkl.HIGHEST_PROTOCOL)
            f.close()

    def _load_pickle(self, name):
        with open(name, 'rb') as f:
            obj = pkl.load(f)
            f.close()
        return obj

    def _save_txt(self, name, obj, **kwargs):
        np.savetxt(name, obj, **kwargs)

    def _load_txt(self, name, **kwargs):
        return np.loadtxt(name, **kwargs)

    def _save_torch(self, name, obj, **kwargs):
        T.save(obj, name, **kwargs)

    def _load_torch(self, name, **kwargs):
        return T.load(name, **kwargs)

    def reset(self):
        """
        factory-resets the monitor object.
        This includes clearing all the collected data,
        set the iteration and epoch counters to 0,
        and reset the timer.

        :return: ``None``.
        """

        self._num_since_beginning = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._num_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._img_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._hist_since_beginning = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._hist_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._pointcloud_since_last_flush = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._options = collections.defaultdict(_spawn_defaultdict_ordereddict)
        self._dump_files = collections.OrderedDict()
        self._iter = 0
        self._last_epoch = 0
        self._timer = time.time()

    def read_log(self, log):
        """
        reads a saved log file.

        :param log:
            name of the log file.
        :return:
            contents of the log file.
        """

        with open(os.path.join(self.current_folder, log), 'rb') as f:
            contents = pkl.load(f)
            f.close()
        return contents
