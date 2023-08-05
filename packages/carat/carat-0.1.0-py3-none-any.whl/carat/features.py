# encoding: utf-8
# pylint: disable=C0103
# pylint: disable=too-many-arguments
"""Functions to compute accentuation features and feature maps."""

import numpy as np
import scipy as sp
from . import util

__all__ = ['accentuation_feature']

def accentuation_feature(signal, fs, sum_flag=True, log_flag=False, mel_flag=True,
                         alpha=1000, maxfilt_flag=False, maxbins=3, **kwargs):
    """Compute accentuation feature from audio signal.


    Based on the log-power Mel spectrogram [1].

    [1] Böck, Sebastian, and Gerhard Widmer.
           "Maximum filter vibrato suppression for onset detection."
           16th International Conference on Digital Audio Effects,
           Maynooth, Ireland. 2013.

        This performs the following calculations to the input signal:

        input->STFT->(Mel scale)->(Log)->(Max filtering)->Diff->HWR->(Sum)

        Parenthesis denote optional steps.

    **Args**:
        - input: signal
        - fs: sampling rate
        - sum_flag (bool): true if the features are to be summed for each frame.
        - log_flag (bool): true if the features energy are to be converted to dB.
        - mel_flag (bool): true if the features are to be mapped in the Mel scale.
        - alpha (int): compression parameter for dB conversion - log10(alpha*abs(S)+1).
        - maxfilt_flag (bool): true if a maximum filtering is applied to the feature.
        - maxbins (int): number of frequency bins for maximum filter size
        - **kw: these keyword arguments are passed down to each of the functions used
    **Returns**:
        - feature (numpy array): feature values
        - time (numpy array): time values

    **Raises**:
        -
    """

    # STFT
    val_kw, remaining_kw = util.getValidKeywords(kwargs, spectrogram)
    feature, time, frequency = spectrogram(signal, fs, **val_kw)
    # mel scale mapping (and absolute value)
    if mel_flag:
        val_kw, remaining_kw = util.getValidKeywords(remaining_kw, melSpectrogram)
        feature, time, frequency = melSpectrogram(feature, time, frequency, **val_kw)
    else:
        # take the absolute value
        feature = sp.absolute(feature)
    # log magnitude (with compression parameter)
    if log_flag:
        feature = 20*sp.log10(alpha * feature + 1)
    # maximum filter (and difference)
    if maxfilt_flag:
        # maximum filter
        max_spec = sp.ndimage.filters.maximum_filter(feature, size=(maxbins, 1))
        # init the diff array
        diff = sp.zeros(feature.shape)
        # calculate difference between log spec and max filtered version
        diff[:, 1:] = (feature[:, 1:] - max_spec[:, : -1])
        # save feature data
        feature = diff
    else:
        # conventional difference (first order)
        feature = calculateDelta(feature, delta_filter_length=1)
    # half-wave rectification
    feature = halfWaveRectification(feature)
    # sum features
    if sum_flag:
        feature = sumFeatures(feature)

    # return
    return feature, time, frequency


def feature_map(feature, time, beats, downbeats, n_beats=4, n_tatums=4,
                norm_flag=True, pnorm=8, window=0.1):
    """Compute feature map from accentuation feature signal.


    Based on the feature map introduced in [1].

    [1] Rocamora, Jure, Biscainho
           "Tools for detection and classification of piano drum patterns from candombe recordings."
           9th Conference on Interdisciplinary Musicology (CIM),
           Berlin, Germany. 2014.


    The accentuation feature is organized into a feature map. First, the feature signal is
    time-quantized to the rhythm metric structure by considering a grid of tatum pulses equally
    distributed within the annotated beats. The corresponding feature value is taken as the maximum
    within window centered at the frame closest to each tatum instant. This yields feature vectors
    whose coordinates correspond to the tatum pulses of the rhythm cycle (or bar). Finally, a
    feature map of the cycle-length rhythmic patterns of the audio file is obtained by building a
    matrix whose columns are consecutive feature vectors.

    **Args**:
        - feature (numpy array): feature signal
        - **kw: these keyword arguments are passed down to each of the functions used
    **Returns**:
        - :

    **Raises**:
        -
    """

    normalized_feature = np.copy(feature)

    if norm_flag:
        # normalize feature values with a p-norm applied within a local window
        normalized_feature = feature_normalization(feature, time, beats,
                                                   n_tatums=n_tatums, pnorm=pnorm)

    # generate tatum grid to time quantize feature values
    tatums = generate_tatum_grid(beats, downbeats, n_tatums)

    # time quantize the feature signal to the tatum grid
    quantized_feature = feature_time_quantize(normalized_feature, time, tatums, window=window)

    # reshape into a matrix whose columns are bars and its elements are tatums
    features_map = np.reshape(quantized_feature, (-1, n_beats*n_tatums))

    return features_map, quantized_feature, tatums, normalized_feature


def feature_normalization(feature, time, beats, n_tatums=4, pnorm=8):
    """Local amplitude normalization of the feature signal.

    Based on the feature map introduced in [1] and detailed in [2].

    [1] Rocamora, Jure, Biscainho
           "Tools for detection and classification of piano drum patterns from candombe recordings."
           9th Conference on Interdisciplinary Musicology (CIM),
           Berlin, Germany. 2014.

    [2] Rocamora, Cancela, Biscainho
           "Information theory concepts applied to the analysis of rhythm in recorded music with
           recurrent rhythmic patterns."
           Journal of the AES, 67(4), 2019.

    A local amplitude normalization is carried out to preserve intensity variations of the
    rhythmic patterns while discarding long-term fluctuations in dynamics. A p-norm within
    a local window is applied. The window width is proportional to the beat period.

    **Args**:
        - feature (numpy array): feature signal values
        - time (numpy array): time instants of the feature values
        - beats (numpy array): time instants of the tactus beats
        - n_tatums (int): number of tatums per tactus beat
        - pnorm (int): p-norm order for normalization
    **Returns**:
        - :

    **Raises**:
        - norm_feature (numpy array): normalized feature signal values
    """

    # estimate tatum period from annotations for normalization
    # time sample interval
    samps_time = time[1] - time[0]
    # compute tatum period in seconds from median of the tactus intervals
    beats_periods = beats[1:] - beats[0:-1]
    # tatum period in seconds
    tatum_period_secs = np.median(beats_periods) / n_tatums
    # period in samples
    tatum_period_samps = int(round(tatum_period_secs / samps_time)) - 1
    # normalize feature
    norm_feature = normalize_features(feature, tatum_period_samps * pnorm, p=pnorm)

    return norm_feature


def generate_tatum_grid(beats, downbeats, n_tatums):
    """Generate tatum temporal grid from time instants of the tactus beats.

    A grid of tatum pulses is generated equally distributed within the given tactus beats.
    The grid is used to time quantize the feature signal to the rhythmic metric structure.

    Parameters
    ----------
    labels_time (np.ndarray) : time instants of the tactus beats
    labels (list)            : labels at the tactus beats (e.g. 1.1, 1.2, etc)

    Returns
    -------
    tatum_time (np.ndarray)  : time instants of the tatum beats
    """

    # first and last downbeat
    first_downbeat = downbeats[0]
    last_downbeat = downbeats[-1]

    # index of first and last downbeat into the beats array
    # NOTE: we assume coincident beats and downbeats (because of our data)
    indx_first = int(np.where(beats == first_downbeat)[0])
    indx_last = int(np.where(beats == last_downbeat)[0])

    # number of tactus beats
    num_beats = indx_last - indx_first # the beat of the last downbeat is not counted

    # time instants of the tatums
    tatums = np.zeros(num_beats * n_tatums)

    # compute tatum time locations from the tactus beats
    for ind in range(indx_first, indx_last):
        # tatum period estimated from tactus beats
        tatum_period = (beats[ind+1] - beats[ind]) / n_tatums
        # a whole bar of tatum beats
        tatum_bar = np.array(range(n_tatums) * tatum_period + beats[ind])
        # save bar of tatum beats
        tatums[(ind*n_tatums):((ind+1)*n_tatums)] = tatum_bar

    return tatums


def feature_time_quantize(feature, time, tatums, window=0.1):
    """Time quantization of the feature signal to a tatum grid.

    The feature signal is time-quantized to the rhythm metric structure by considering a grid of
    tatum pulses equally distributed within the tactus beats. The feature value assigned to each
    tatum time instant is obtained as the maximum value of the feature signal within a certain
    window centered at the tatum time instant. Default value for the total window lenght is 100 ms.

    **Args**:
        - feature (numpy array): feature signal values
        - time (numpy array): time instants of the feature values
        - tatums (numpy array): time instants of the tatum grid
    **Returns**:
        - :

    **Raises**:
        - quantized_feature (numpy array): time quantized feature signal values
    """
    # number of tatum instants
    num_tatums = tatums.size

    # time quantized feature values at tatum instants
    quantized_feature = np.zeros(tatums.shape)

    # compute hop size to set time-quantization window
    hop_size = time[1] - time[0]
    # number of frames within time quantization window
    win_num_frames = int(window / hop_size)
    # half window in frames
    hwf = int(np.floor(win_num_frames / 2))
    # check if it is even to center window
    if hwf % 2 != 0:
        hwf -= 1

    # compute feature value considering a certain neighbourhood
    for ind in range(num_tatums):
        # closest feature frame to tatum instant
        ind_tatum = util.find_nearest(time, tatums[ind])
        # get maximum feature value within a neighbourhood
        if ind_tatum == 0:
            quantized_feature[ind] = np.max(feature[ind_tatum:ind_tatum+hwf+1])
        else:
            quantized_feature[ind] = np.max(feature[ind_tatum-hwf:ind_tatum+hwf+1])

    return quantized_feature

def spectrogram(signal, fs, window_length=20e-3, hop=10e-3,
                windowing_function=sp.hanning, dft_length=None, zp_flag=False):
    """ Calculates the Short-Time Fourier Transform a signal.

    Given an input signal, it calculates the DFT of frames of the signal and stores them
    in bi-dimensional Scipy array.

    **Args**:
        - window_len (float):length of the window in seconds (must be positive).
        - window (callable): a callable object that receives the window length in samples
          and returns a numpy array containing the windowing function samples.
        - hop (float): frame hop between adjacent frames in seconds.
        - zp_flag (bool): a flag indicating if the *Zero-Phase Windowing* should be
          performed.

    **Returns**:
        - spec (numpy array): spectrogram data
        - time (numpy array): time in seconds of each frame
        - frequnecy (numpy array): frequency grid

    """
    # Converting window_length and hop from seconds to number of samples:
    win_samps = int(round(window_length * fs))
    hop_samps = max(int(round(hop * fs)), 1)
    spec, time, frequency = util.STFT(signal, win_samps, hop_samps,
                                      windowing_function, dft_length, zp_flag)
    # convert indices to seconds and Hz
    time /= fs
    frequency *= fs
    # return
    return spec, time, frequency


def melSpectrogram(in_spec, in_time, in_freq, nfilts=40, minfreq=20, maxfreq=None):
    """This function converts a Spectrogram with linearly spaced frequency components
    to the Mel scale.

        Given an input signal, it calculates the DFT of frames of the signal and stores
        them in bi-dimensional Scipy array.


    **Args**:
        - window_len (float): length of the window in seconds (must be positive).
        - window (callable): a callable object that receives the window length in samples
          and returns a numpy array containing the windowing function samples.
    **Returns**:
        - spec (numpy array): mel-spectrogram data
        - time (numpy array): time in seconds of each frame
        - frequnecy (numpy array): frequency grid

    """
    if maxfreq is None:
        maxfreq = max(in_freq)
    (wts, frequency) = util.fft2mel(in_freq, nfilts, minfreq, maxfreq)
    spec = sp.dot(wts, sp.sqrt(sp.absolute(in_spec)**2))
    time = in_time

    # return
    return spec, time, frequency


def halfWaveRectification(in_signal):
    """ Half-wave rectifies features.

        All feature values below zero are assigned to zero.

    **Args**:
        - input: feature object
        - delta_filter_length (int): length of the filter used to calculate the Delta
          coefficients. Must be an odd number.
    **Returns**:
        - output: numpy array
        A :class:`Feature` object containing the result of the calculation.

    **Raises**:
        - ValueError when the input features are complex.
    """
    out_signal = np.copy(in_signal)
    if out_signal.dtype != complex:
        out_signal[out_signal < 0] = 0.0
    else:
        raise ValueError('Cannot half-wave rectify a complex signal.')
    return out_signal


def calculateDelta(in_signal, delta_filter_length=3):
    """ This function calculates the delta coefficients of a given feature.

    **Args**:
        - input: input feature signal
        - delta_filter_length (int): length of the filter used to calculate the Delta
          coefficients. Must be an odd number.
    **Returns**:
        - output: output feature signal
    """
    out_signal = np.copy(in_signal)
    out_signal = util.deltas(out_signal, delta_filter_length)
    return out_signal


def sumFeatures(in_signal):
    """ This function sums all features along frames.

    **Args**:
        - input: input feature signal
    **Returns**:
        - output: output feature signal
    """
    out_signal = np.copy(in_signal)
    out_signal = sp.sum(out_signal, axis=0)
    return out_signal


def def_norm_feat_gen(data, max_period, p):
    """ Normalization of the feature signal using p-norm.
    """
    if not max_period  % 2:
        max_period += 1
    ext_len = int((max_period - 1) / 2)
    ext_data = data[1:ext_len + 1][::-1]
    ext_data = sp.append(ext_data, data)
    ext_data = sp.append(ext_data, data[-2:-ext_len - 2:-1])

    def aux(i, win_size):
        fac = int(win_size % 2)
        h_len = int(win_size / 2)
        aux = sp.linalg.norm(ext_data[i - h_len + ext_len : i + ext_len + h_len + fac], ord=p)
        return ext_data[i + ext_len] / max(aux, 1e-20)

    return aux


def normalize_features(data, win_len, p):
    """ Normalization of the feature signal using p-norm.
    """
    aux = def_norm_feat_gen(data, win_len, p)
    out = data.copy()
    for i in range(data.size):
        out[i] = aux(i, win_len)
    return out


#def accentuation_feature(y, sr=22050, hop_length=512, n_fft=2048,
#                         n_mels=128, freq_sb=None, **kwargs):
#    """Compute accentuation feature from audio signal.
#
#
#    Based on the log-power Mel spectrogram [1].
#
#    [1] Böck, Sebastian, and Gerhard Widmer.
#           "Maximum filter vibrato suppression for onset detection."
#           16th International Conference on Digital Audio Effects,
#           Maynooth, Ireland. 2013.
#
#    In current implementation win_length = n_fft (because of librosa)
#    The log-power Mel spectrogram is computed for the full spectrum,
#    i.e. up to sr/2 but fmin and fmax could be used to limit the representation.
#
#    A frequency band to focus on.
#
#    Parameters
#    ----------
#
#    Returns
#    -------
#
#    Examples
#    --------
#
#    Notes
#    -----
#    """
#
#    if freq_sb is None:
#        # compute feature values for the full spectrum
#        feature_values = librosa.onset.onset_strength(y=y, sr=sr, n_fft=n_fft, n_mels=n_mels,
#                                                      hop_length=hop_length, **kwargs)
#    else:
#        # check if two frequency values are provided
#        if isinstance(freq_sb, np.ndarray) and freq_sb.shape[0] == 2:
#
#            # compute the frequency of the mel channels
#            n_freqs = librosa.core.time_frequency.mel_frequencies(n_mels=n_mels, fmin=0.0,
#                                                                  fmax=sr/2, htk=False)
#            # find indexes of sub-band channels
#            channels = [util.find_nearest(n_freqs, freq) for freq in freq_sb]
#            # compute feature values for the full spectrum and aggregate across a sub-band
#            feature_values = librosa.onset.onset_strength_multi(y=y, sr=sr,
#                                                                n_fft=n_fft,
#                                                                n_mels=n_mels,
#                                                                hop_length=hop_length,
#                                                                channels=channels,
#                                                                **kwargs)
#            # save a single sub-band
#            feature_values = feature_values[0]
#
#    # compute time instants of the feature values
#    times = librosa.frames_to_time(np.arange(feature_values.shape[0]), sr=sr,
#                                   n_fft=n_fft, hop_length=hop_length)
#    # remove offset of n_fft/2 and hop_length because of the time lag for computing differences
#    times = times - (n_fft/2/sr) - (hop_length/sr)
#    # times = (np.arange(feature_values.shape[0]) * hop_length + win_length/2) / sr
#
#    return feature_values, times
