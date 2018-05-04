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


# part 3
def uniform_sum():
    sum_list = [sum(np.random.uniform(0,1,10)) for i in range(10000)]
    plt.hist(sum_list)
    plt.show()
    #print(sum_list)

    if __name__ == '__main__':
        pass