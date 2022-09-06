import numpy as np 
import matplotlib.pyplot as plt
import os

from scipy.signal import tukey, butter, sosfiltfilt


def _butter_bandpass(lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    if low < 0:
        Wn = high
        btype = "lowpass"
    elif high < 0:
        Wn = low
        btype = "highpass"
    else:
        Wn = [low, high]
        btype = "bandpass"

    sos = butter(order, Wn, btype=btype, output="sos")
    return sos

def taper_filter(arr, fmin, fmax, samp_DAS, order=2):

    window_time = tukey(arr.shape[-1], 0.1)
    arr_wind = arr * window_time

    sos = _butter_bandpass(fmin, fmax, samp_DAS, order)
    arr_filt = sosfiltfilt(sos, arr_wind, axis=-1)

    return arr_filt

samp = 400
gauge = 3.2

cwd = os.getcwd()

car = plt.imread(os.path.join(cwd, "data", "Sedan-car.png"))
data = np.load(os.path.join(cwd, "data", "car_unfilt.npy"))

data_low = taper_filter(data, fmin=0.1, fmax=2, samp_DAS=samp) * 1e-3
data_high = taper_filter(data, fmin=5, fmax=20, samp_DAS=samp) * 1e-3

x = np.arange(data.shape[0] * gauge * 1e-3)
t = np.arange(data.shape[1]) / samp


def generate_circle(x0, y0, radius):
    x = np.linespace(-radius, radius, 1000)
    y = np.sqrt(radius**2 - x**2)
    return x + x0, y + y0

font_dict = {
        "fontsize": 10,
        "va": "top",
        "ha": "center",
}

letter_params = {
        "fontsize": 10,
        "verticalalignment": "top",
        "horizontalalignment": "left",
        "bbox": {"edgecolor": "k", "linewidth": 1, "facecolor": "w",}
}


c_cable = "xkcd:golden yellow"
c_static = "c"
c_dynamic = "xkcd:vermillion"
c_subsurface = "xkcd:slate"

x0_1 = 500
x0_2 = 2200
y0 = 850

ch_select = 95

plt.close("all")
fig = plt.figure(figsize=(9, 10))
gs = fig.add_gridspec(5, 2)

ax = fig.add_subplot(gs[:2, :])

ax.imshow(car)
