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


# part 5
def time_sort(some_list):
    start_time = time.time()
    some_list = sorted(some_list)
    end_time = time.time()
    return end_time - start_time

def sum_sort(some_list):
    start_time = time.time()
    some_list = sum(some_list)
    end_time = time.time()
    return end_time - start_time

def plot_lists():
    # generate lists
    one = [random.random()]
    ten = [random.random() for i in range(10)]
    hund = [random.random() for i in range(100)]
    thou = [random.random() for i in range(1000)]
    ten_thou = [random.random() for i in range(10000)]
    hund_thou = [random.random() for i in range(100000)]
    mill = [random.random() for i in range(1000000)]

    # sort time plots
    t_one = time_sort(one)
    t_ten = time_sort(ten)
    t_hund = time_sort(hund)
    t_thou = time_sort(thou)
    t_ten_thou = time_sort(ten_thou)
    t_hund_thou = time_sort(hund_thou)
    t_mill = time_sort(mill)

    # create a list of times to sort lists
    time_list = [t_one, t_ten, t_hund, t_thou, t_ten_thou, t_hund_thou, t_mill]
    #print(time_list)
    
    # sum time plots
    t_one = sum_sort(one)
    t_ten = sum_sort(ten)
    t_hund = sum_sort(hund)
    t_thou = sum_sort(thou)
    t_ten_thou = sum_sort(ten_thou)
    t_hund_thou = sum_sort(hund_thou)
    t_mill = sum_sort(mill)

    # create a list of times to sum lists
    sum_list = [t_one, t_ten, t_hund, t_thou, t_ten_thou, t_hund_thou, t_mill]
    #print(sum_list)

    elements = [1, 10, 100, 1000, 10000, 100000, 1000000]

    # plot both graphs
    plt.figure(1)
    plt.subplot(211)
    plt.plot(time_list, elements)
    plt.title('Time to sort elements')
    plt.xlabel('Time')
    plt.ylabel('Elements')

    #plt.figure(2)
    plt.subplot(212)
    plt.plot(sum_list, elements)
    plt.title('Time to sum elements')
    plt.xlabel('Time')
    plt.ylabel('Elements')

    plt.show()
    

    if __name__ == '__main__':
        pass