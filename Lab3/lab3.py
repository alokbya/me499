#!/usr/bin/env python

"""
Alaaddin Alokby
Lab3: PyPlot
Sources:    https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
            https://docs.python.org/3/library/timeit.html
"""

import matplotlib.pyplot as plt
import numpy as np 
from math import pi
import random
import msd
import time
# import plotting files
import part2
import part3
import part4
import part5


if __name__ == '__main__':
    part2.plot_sine()
    part3.uniform_sum()
    part4.show_msd()
    part5.plot_lists()