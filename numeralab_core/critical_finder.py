import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

def find_critical_points(x_vals, y_vals):
    # Lokalde maksimum ve minimum noktaları bul
    maxima = argrelextrema(y_vals, np.greater)[0]
    minima = argrelextrema(y_vals, np.less)[0]

    crit_points = {
        "maxima": list(zip(x_vals[maxima], y_vals[maxima])),
        "minima": list(zip(x_vals[minima], y_vals[minima]))
    }

    # Grafik çiz
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="Function")
    ax.plot(x_vals[maxima], y_vals[maxima], 'ro', label='Local Maxima')
    ax.plot(x_vals[minima], y_vals[minima], 'go', label='Local Minima')
    ax.axhline(0, color='gray', linestyle='--')
    ax.legend()

    return crit_points, fig
