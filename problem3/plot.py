import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib import image

import random


def draw_spline(t, c, k):
    t_arr = np.linspace(0, t, 2*k + 2)
    c_arr = random.sample(range(0, 2*k), k+1)
    spl = interpolate.BSpline(t_arr, c_arr, k)

    fig, ax = plt.subplots()
    xx = np.linspace(0, c, 10)
    ax.plot(xx, spl(xx), 'b-', label='BSpline')
    ax.grid(True)
    plt.axis('off')
    #data = image.imread('static/images/plot_bg.jpg')
    #plt.imshow(data)
    #plt.show()
    plt.savefig('static/images/plot.jpg')


if __name__ == '__main__':
    draw_spline(10, 5, 6)