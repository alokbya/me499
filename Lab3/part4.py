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


# part 4
def show_msd():
    smd = msd.MassSpringDamper(10, 5, 2)
    state,time = smd.simulate(0.0, 1.0)
    # create y axis variable equal to the pos state
    y = [state[i][0] for i in range(len(state) -1)]
    # create x axis variable equal to the time
    x = [time[i] for i in range(len(time) - 1)]
    plt.plot(x, y)
    plt.title('Mass Spring Damper Plot')
    plt.ylabel('Displacement')
    plt.xlabel('Time')
    plt.show()

    if __name__ == '__main__':
        pass