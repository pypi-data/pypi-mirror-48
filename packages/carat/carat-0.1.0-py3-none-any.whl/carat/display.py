# encoding: utf-8
# pylint: disable=C0103
# pylint: disable=too-many-arguments
"""Utility functions to deal with audio."""

import warnings
import numpy as np
import librosa.display
from matplotlib.cm import gray_r
from matplotlib.axes import Axes
from pylab import get_cmap
from matplotlib import colors
from matplotlib.ticker import Formatter
from . import util

__all__ = ['waveplot', 'specshow', 'mapshow']

# simply use librosa.specshow (this may change in the future)
specshow = librosa.display.specshow


def waveplot(y, sr=22050, x_axis='time', beats=None, beat_labs=None,
             ax=None, **kwargs):
    '''Plot an audio waveform and beat labels (optinal).


    Parameters
    ----------
    y : np.ndarray
        audio time series

    sr : number > 0 [scalar]
        sampling rate of `y`

    x_axis : str {'time', 'off', 'none'} or None
        If 'time', the x-axis is given time tick-marks.

    ax : matplotlib.axes.Axes or None
        Axes to plot on instead of the default `plt.gca()`.

    kwargs
        Additional keyword arguments to `matplotlib.`

    Returns
    -------

    See also
    --------


    Examples
    --------
    '''

    kwargs.setdefault('color', 'royalblue')
    kwargs.setdefault('linestyle', '-')
    kwargs.setdefault('alpha', 0.6)

    if y.ndim > 1:
        raise ValueError("`y` must be a one dimensional array. "
                         "Found y.ndim={}".format(y.ndim))

    # time array in seconds
    time = np.arange(y.size)/sr
    # its maximum value
    max_time = np.max(time)

    # check axes and create it if needed
    axes = __check_axes(ax)

    # plot waveform
    out = axes.plot(time, y, **kwargs)

    if beats is not None:
        __plot_beats(beats, max_time, axes, beat_labs=beat_labs, **kwargs)

    # format x axis
    if x_axis == 'time':
        axes.xaxis.set_major_formatter(TimeFormatter(lag=False))
        axes.xaxis.set_label_text('Time (s)')
    elif x_axis is None or x_axis in ['off', 'none']:
        axes.set_xticks([])
    else:
        raise ParameterError('Unknown x_axis value: {}'.format(x_axis))

    return out


def featureplot(feature, time, x_axis='time', beats=None, beat_labs=None,
                ax=None, **kwargs):
    '''Plot an audio waveform and beat labels (optinal).


    Parameters
    ----------
    feature : np.ndarray
        feature time series

    time : np.ndarray
        time instant of the feature values

    x_axis : str {'time', 'off', 'none'} or None
        If 'time', the x-axis is given time tick-marks.

    ax : matplotlib.axes.Axes or None
        Axes to plot on instead of the default `plt.gca()`.

    kwargs
        Additional keyword arguments to `matplotlib.`

    Returns
    -------

    See also
    --------


    Examples
    --------
    '''

    kwargs.setdefault('color', 'seagreen')
    kwargs.setdefault('linestyle', '-')
    kwargs.setdefault('alpha', 0.8)

    if feature.ndim > 1:
        raise ValueError("`feature` must be a one dimensional array. "
                         "Found feature.ndim={}".format(feature.ndim))

    # maximum time value
    max_time = np.max(time)

    # check axes and create it if needed
    axes = __check_axes(ax)

    # plot waveform
    out = axes.plot(time, feature, **kwargs)

    if beats is not None:
        __plot_beats(beats, max_time, axes, beat_labs=beat_labs, **kwargs)

    # format x axis
    if x_axis == 'time':
        axes.xaxis.set_major_formatter(TimeFormatter(lag=False))
        axes.xaxis.set_label_text('Time (s)')
    elif x_axis is None or x_axis in ['off', 'none']:
        axes.set_xticks([])
    else:
        raise ParameterError('Unknown x_axis value: {}'.format(x_axis))

    return out


def __plot_beats(beats, max_time, ax, beat_labs=None, **kwargs):
    '''Plot beat labels.


    Parameters
    ----------
    beats : np.ndarray
        audio time series

    beat_labs : list
        beat labels

    x_axis : str {'time', 'off', 'none'} or None
        If 'time', the x-axis is given time tick-marks.

    ax : matplotlib.axes.Axes or None
        Axes to plot on instead of the default `plt.gca()`.

    kwargs
        Additional keyword arguments to `matplotlib.`

    Returns
    -------

    See also
    --------


    Examples
    --------
    '''

    kwargs['color'] = 'black'
    kwargs.setdefault('linestyle', '-')
    kwargs['alpha'] = 0.3
    kwargs.setdefault('linewidth', 2)

    # consider beats (and labels) bellow max_time
    ind_beat = util.find_nearest(beats, max_time)
    new_beats = beats[:ind_beat]
    if beat_labs is not None:
        new_labs = beat_labs[:ind_beat]

    # plot beat annotations
    for beat in new_beats:
        ax.axvline(x=beat, **kwargs)

    # set ticks and labels
    ax2 = ax.twiny()
    ax2.set_xlim(ax.get_xlim())
    ax2.set_xticks(new_beats)
    ax2.set_xticklabels(new_labs)
    #ax2.set_xlabel("beats")

    return ax2


def mapshow(data, x_coords=None, y_coords=None, ax=None,
            n_tatums=4, clusters=None, **kwargs):
    '''Display a feature map.

    Parameters
    ----------
    data : np.ndarray
        Feature map to display

    x_coords : np.ndarray [shape=data.shape[1]+1]
    y_coords : np.ndarray [shape=data.shape[0]+1]

        Optional positioning coordinates of the input data.

    ax : matplotlib.axes.Axes or None
        Axes to plot on instead of the default `plt.gca()`.

    n_tatums : int
        Number of tatums (subdivisions) per tactus beat

    clusters : np.ndarray
        Array indicating cluster number for each pattern of the input data.
        If provided (not None) the clusters area displayed with colors.

    kwargs : additional keyword arguments
        Arguments passed through to `matplotlib.pyplot.pcolormesh`.

        By default, the following options are set:

            - `cmap=gray_r`
            - `rasterized=True`
            - `edgecolors='None'`
            - `shading='flat'`

    Returns
    -------
    axes
        The axis handle for the figure.


    See Also
    --------
    matplotlib.pyplot.pcolormesh


    Examples
    --------

    '''

    kwargs.setdefault('cmap', gray_r)
    kwargs.setdefault('rasterized', True)
    kwargs.setdefault('edgecolors', 'None')
    kwargs.setdefault('shading', 'flat')

    # number of bars
    bars = data.shape[0]
    # number of tatums in a bar
    tatums = data.shape[1]

    # set the x and y coordinates
    y_coords = np.array(range(tatums+1))+0.5
    x_coords = np.array(range(bars))+1

    # check axes and create it if needed
    axes = __check_axes(ax)
    # plot rhythmic patterns map (grayscale)
    out = axes.pcolormesh(x_coords, y_coords, data.T, **kwargs)
    __set_current_image(ax, out)

    # if clusters are given then show them in colors
    if clusters is not None:
        # check clusters and return number of clusters
        n_clusters = __check_clusters(clusters, bars)
        # matrix and other elements needed to plot clusters' map
        mapc, cmap, norm = __get_cluster_matrix(clusters, n_clusters, y_coords.size)
        # plot clusters in colors
        axes.pcolormesh(x_coords, y_coords, mapc, cmap=cmap, norm=norm, alpha=0.6)

    # set axes limits
    axes.set_xlim(x_coords.min()-0.5, x_coords.max()+0.5)
    axes.set_ylim(y_coords.min(), y_coords.max())


    # configure tickers and labels
    __decorate_axis_map(axes, tatums=n_tatums)

    return axes


def __check_axes(axes):
    '''Check if "axes" is an instance of an axis object.'''
    if axes is None:
        import matplotlib.pyplot as plt
        axes = plt.gca()
    elif not isinstance(axes, Axes):
        raise ValueError("`axes` must be an instance of matplotlib.axes.Axes. "
                         "Found type(axes)={}".format(type(axes)))
    return axes

def __check_clusters(clusters, bars):
    '''Check if "clusters" is an instance of an axis object.
       Check if "clusters" is a one dimensional array of the correct length.
       '''
    if isinstance(clusters, np.ndarray):
        if clusters.ndim == 1:
            if clusters.size == bars:
                # count number of clusters
                n_clusters = np.unique(clusters).size
        else:
            raise ValueError("`clusters` must be a one dimensional array. "
                             "Found clusters.ndim={}".format(clusters.ndim))
    else:
        raise ValueError("`clusters` must be an instance of numpy.ndarray. "
                         "Found type(axes)={}".format(type(clusters)))

    return n_clusters


def __get_cluster_matrix(clusters, n_clusters, n_tatums):
    '''Get clusters' matrix and other elements needed to plot clusters' map.'''
    # make a color map of fixed colors for colormesh
    # cmap = get_cmap('RdBu', n_clusters)
    cmap = get_cmap('tab10', n_clusters)
    bounds = range(n_clusters+1)
    norm = colors.BoundaryNorm(bounds, cmap.N)
    mapc = np.tile(clusters+0.5, (n_tatums, 1))

    return mapc, cmap, norm


def __set_current_image(ax, img):
    '''Helper to set the current image in pyplot mode.

    If the provided `ax` is not `None`, then we assume that the user is using the object API.
    In this case, the pyplot current image is not set.
    '''

    if ax is None:
        import matplotlib.pyplot as plt
        plt.sci(img)


def __decorate_axis_map(axis, tatums=4):
    '''Configure axis ticks and labels for feature map plot'''

    # ticks at beats
    ylims = axis.get_ylim()
    all_tatums = int(ylims[1])
    ticks_beats = [x+0.5 for x in range(0, all_tatums, tatums)]
    num_beats = int(all_tatums / tatums)
    labels_beats = [x+1 for x in range(num_beats)]

    axis.yaxis.set_ticks(ticks_beats)
    axis.set_yticklabels(labels_beats)
    axis.tick_params(labelsize=10)
    # axis.yaxis.set_major_formatter(NullFormatter())
    axis.yaxis.grid()
    gridlines = axis.get_ygridlines()
    for line in gridlines:
        line.set_linestyle('-')
        line.set_linewidth(2)
        line.set_color('black')
    axis.set_ylabel('beats')


class TimeFormatter(Formatter):
    '''A tick formatter for time axes. Copied from librosa.

    Automatically switches between seconds, minutes:seconds,
    or hours:minutes:seconds.

    Parameters
    ----------
    lag : bool
        If `True`, then the time axis is interpreted in lag coordinates.
        Anything past the midpoint will be converted to negative time.

    unit : str or None
        Abbreviation of the physical unit for axis labels and ticks.
        Either equal to `s` (seconds) or `ms` (milliseconds) or None (default).
        If set to None, the resulting TimeFormatter object adapts its string
        representation to the duration of the underlying time range:
        `hh:mm:ss` above 3600 seconds; `mm:ss` between 60 and 3600 seconds;
        and `ss` below 60 seconds.


    See also
    --------
    matplotlib.ticker.Formatter


    Examples
    --------

    For normal time

    >>> import matplotlib.pyplot as plt
    >>> times = np.arange(30)
    >>> values = np.random.randn(len(times))
    >>> plt.figure()
    >>> ax = plt.gca()
    >>> ax.plot(times, values)
    >>> ax.xaxis.set_major_formatter(librosa.display.TimeFormatter())
    >>> ax.set_xlabel('Time')

    Manually set the physical time unit of the x-axis to milliseconds

    >>> times = np.arange(100)
    >>> values = np.random.randn(len(times))
    >>> plt.figure()
    >>> ax = plt.gca()
    >>> ax.plot(times, values)
    >>> ax.xaxis.set_major_formatter(librosa.display.TimeFormatter(unit='ms'))
    >>> ax.set_xlabel('Time (ms)')

    For lag plots

    >>> times = np.arange(60)
    >>> values = np.random.randn(len(times))
    >>> plt.figure()
    >>> ax = plt.gca()
    >>> ax.plot(times, values)
    >>> ax.xaxis.set_major_formatter(librosa.display.TimeFormatter(lag=True))
    >>> ax.set_xlabel('Lag')
    '''

    def __init__(self, lag=False, unit=None):

        if unit not in ['s', 'ms', None]:
            raise ParameterError('Unknown time unit: {}'.format(unit))

        self.unit = unit
        self.lag = lag

    def __call__(self, x, pos=None):
        '''Return the time format as pos'''

        _, dmax = self.axis.get_data_interval()
        vmin, vmax = self.axis.get_view_interval()

        # In lag-time axes, anything greater than dmax / 2 is negative time
        if self.lag and x >= dmax * 0.5:
            # In lag mode, don't tick past the limits of the data
            if x > dmax:
                return ''
            value = np.abs(x - dmax)
            # Do we need to tweak vmin/vmax here?
            sign = '-'
        else:
            value = x
            sign = ''

        if self.unit == 's':
            s = '{:.3g}'.format(value)
        elif self.unit == 'ms':
            s = '{:.3g}'.format(value * 1000)
        else:
            if vmax - vmin > 3600:
                s = '{:d}:{:02d}:{:02d}'.format(int(value / 3600.0),
                                                int(np.mod(value / 60.0, 60)),
                                                int(np.mod(value, 60)))
            elif vmax - vmin > 60:
                s = '{:d}:{:02d}'.format(int(value / 60.0),
                                         int(np.mod(value, 60)))
            else:
                s = '{:.2g}'.format(value)

        return '{:s}{:s}'.format(sign, s)
