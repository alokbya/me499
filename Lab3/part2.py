#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np 
from math import pi
import random
import msd
import time

"""
Alaaddin Alokby
Lab3: PyPlot
Sources:    https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
            https://docs.python.org/3/library/timeit.html
"""


# part 2
def plot_sine():
    # build x and y ranges
    x = np.arange(0, 4*pi, 0.1)
    y = np.sin(x)
    # plot
    plt.plot(x,y)
    # create labels
    plt.ylabel('Sin(x)')
    plt.xlabel('Domain')
    plt.title('Graph of Sin(x)')
    # show plot
    plt.show()

    if __name__ == '__main__':
        pass