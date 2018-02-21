'''
Author: Tiffany Xiao
Date: February 15, 2018

Objective of challenge:
Given a sequence of (integer, positive-valued) item weights,
identify whether or not there is a subset that could fill a
Prime Pantry Box to exactly 100%

How your function should run:
primePantry(list, n_items, total)

Test Cases:
Trial 1: 10 items
Trial 2: 500 items
Trial 3: 10000 items
If correct, run 1000 times, keep best

About the test machine:
MacOS
4 cores
max. recursion depth 1000

Auther notes:

'''
import sys

def primePantry(list_items, n_items, total) :
    ''' Function identifies whether or not there is a subset that could fill a
    Prime Pantry Box to exactly 100%

    list_items - list of all item weights (integer, positive valued)
    n_items - number of items in list_items
    total - total/sum requested (100 in this challenge)
    '''
    # create list of ints with list_items
    list_items = [int(i) for i in range(len(list_items))]

    # return True if there's an element equal to total
    subset = [[True] * (total+1)] * (n_items+1)

    # if the total is 0, return true
    for i in range(0, n_items+1) :
        subset[i][0] = True

    # if the total is not 0 and there is nothing in the list, then its False
    for i in range(1, total + 1) :
        subset[0][i] = False

    # create a 2D array, and fill it up from bottom up. The value of the element
    # is true if there is a subset with total equal to i, or else it's false
    for i in range(1, n_items+1) :
        for j in range(1, total+1) :
            if(j < list_items[i-1]) :
                subset[i][j] = subset[i-1][j]
            if (j >= list_items[i-1]) :
                subset[i][j] = subset[i-1][j] or subset[i - 1][j-list_items[i-1]]

    return subset[n_items][total]

primePantry(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
