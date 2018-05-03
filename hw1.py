#!/usr/bin/env python
"""
Name: Alaaddin Alokby
HW: 1
Date: 5/1/2018
Sources: 
Pandas documentation cited in 'final_stats' function
"""


import csv
import pandas as pd
import numpy as np
import re
import math


def final_stats(filename):
    """
    This function is written for problem 2 of assignment
    Pandas documentation for read_csv()
    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
    
    """
    # open csv
    data = pd.read_csv(filename, skipinitialspace=True)
    
    # get the average final score
    ave = round(np.average(data['Final Score']), 2)
    
    # percent of students above average
    i = 0
    for score in data['Final Score']:
        if score > ave:
            i += 1
    above_ave = str(round(100*i/data['Final Score'].count(), 2)) + '%'
    
    # get median final score
    med = round(np.median(data['Final Score']), 2)
    
    # percent of students above median
    j = 0
    for score in data['Final Score']:
        if score > med:
            j += 1
    above_med = str(round(100*j/data['Final Score'].count(), 2)) + '%'
    output = 'Average Score: ' + str(ave) + '\n' + 'Above Average: ' + above_ave + '\n' + 'Median Score: ' + str(med) + '\n' + 'Above Median: ' + above_med + '\n'
    return output

def hardest_assignment(filename):
    # open csv
    # na_values handles the 'EX' in spreadsheet
    data = pd.read_csv(filename, skipinitialspace=True, na_values=['EX'])

    # create a list of column headers
    headers = []

    # store all homework column headers into 'headers'
    for header in data.keys():
        # if the header contains 'Homework' append to 'headers'
        if(re.match('Homework [\w+\d+]*', header)):
            headers.append(header)
    
    # create a dictionary to hold average scores for each assignment
    ass_avg = {}
    max_score = {}
    min_score = {}
    total_max = {}

    # create new key value pair for each assignment 
    for header in headers:
        ass_avg[header] = round(data[header].mean(), 5)
        max_score[header] = round(max(data[header]), 5)
        min_score[header] = round(min(data[header]), 5)
    

    for header in headers:
        total_max[header] = round(ass_avg[header]/max_score[header], 5)

    hardest = min(total_max, key=total_max.get)
    return 'Hardest Assignment: ' + str(hardest) + '\n'

def hardest_lab(filename):
    # open csv
    # na_values handles the 'EX' in spreadsheet
    data = pd.read_csv(filename, skipinitialspace=True, na_values=['EX'])

    # create a list of column headers
    headers = []

    # store all homework column headers into 'headers'
    for header in data.keys():
        # if the header contains 'Homework' append to 'headers'
        if(re.match('Lab [\w+\d+]*', header)):
            headers.append(header)
    
    # create a dictionary to hold average scores for each assignment
    ass_avg = {}
    max_score = {}
    min_score = {}
    total_max = {}

    # create new key value pair for each assignment 
    for header in headers:
        ass_avg[header] = round(data[header].mean(), 2)
        max_score[header] = round(max(data[header]), 2)
        min_score[header] = round(min(data[header]), 2)
    

    for header in headers:
        total_max[header] = round(ass_avg[header]/max_score[header], 2)

    hardest = min(total_max, key=total_max.get)
    return 'Hardest Lab: ' + str(hardest) + '\n'

def get_grades(filename):
    # create gradebook dict to store number of students with each grade
    grade_book = {
        'A': 0,
        'A-': 0,
        'B+': 0,
        'B': 0,
        'B-': 0,
        'C+': 0,
        'C': 0,
        'C-': 0,
        'D+': 0,
        'D': 0,
        'D-': 0,
        'F': 0
    }
    data = pd.read_csv(filename, skipinitialspace=True, na_values=['EX'])
    for grade in data['Final Score']:
        if(grade >= 94):
            grade_book['A'] += 1
        elif(grade < 94 and grade >= 90):
            grade_book['A-'] += 1
        elif(grade < 90 and grade >= 87):
            grade_book['B+'] += 1
        elif(grade < 87 and grade >= 84):
            grade_book['B'] += 1
        elif(grade < 84 and grade >= 80):
            grade_book['B-'] += 1
        elif(grade < 80 and grade >= 77):
            grade_book['C+'] += 1
        elif(grade < 77 and grade >= 74):
            grade_book['C'] += 1
        elif(grade < 74 and grade >= 70):
            grade_book['C-'] += 1
        elif(grade < 70 and grade >= 67):
            grade_book['D+'] += 1
        elif(grade < 67 and grade >= 64):
            grade_book['D'] += 1
        elif(grade < 64 and grade >= 61):
            grade_book['D-'] += 1
        else:
            grade_book['F'] += 1

    for key in grade_book:
        print(str(key) + '\t' + str(grade_book[key]))

    return ''

def get_complainers(filename):
    # get data from file
    data = pd.read_csv(filename, skipinitialspace=True, na_values=['EX'])
    # create variable to store num of complainers
    complainer = 0
    for grade in data['Final Score']:
        if(grade < 94 and grade >= 94-0.5):
            complainer += 1
        elif(grade < 90 and grade >= 90-0.5):
            complainer += 1
        elif(grade < 87 and grade >= 87-0.5):
            complainer += 1
        elif(grade < 84 and grade >= 84-0.5):
            complainer += 1
        elif(grade < 80 and grade >= 80-0.5):
            complainer += 1
        elif(grade < 77 and grade >= 77-0.5):
            complainer += 1
        elif(grade < 74 and grade >= 74-0.5):
            complainer += 1
        elif(grade < 70 and grade >= 70-0.5):
            complainer += 1
        elif(grade < 67 and grade >= 67-0.5):
            complainer += 1
        elif(grade < 64 and grade >= 64-0.5):
            complainer += 1
        
    return str(complainer) + ' students will complain about their grade. \n'

def get_round_grades(filename):

    data = pd.read_csv(filename, skipinitialspace=True, na_values=['EX'])

    # create a list to store nameless grades
    all_grades = []
    for each_grade in data['Final Score']:
        all_grades.append(each_grade)
    
    # sort the grades in ascending order
    all_grades = sorted(all_grades, key=float, reverse=True)

    a = all_grades[math.floor(0.1*len(all_grades) - 1)]
    b = all_grades[math.floor(0.3*len(all_grades) - 1) ]
    c = all_grades[math.floor(0.6*len(all_grades) - 1)]
    d = all_grades[math.floor(0.9*len(all_grades) - 1)]
    #f = all_grades[math.floor(0.9*len(all_grades) - 1)]
    return 'A \t' + str(a) + '\nB \t' + str(b) +\
    '\nC \t' + str(c) + '\nD \t' + str(d) \
    # + '\nF \t' + str(f)

if __name__ == '__main__':

    print(final_stats('grades.csv'))
    print(hardest_assignment('grades.csv'))
    print(hardest_lab('grades.csv'))
    print(get_grades('grades.csv'))
    print(get_complainers('grades.csv'))
    print(get_round_grades('grades.csv'))