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
    list_items = [int(i) for i in list_items.strip('[]').split(',')]

    # check for some cases in which we do not need to run the entire function
    if total < 0 or total > sum(list_items):
        print("False")
        sys.exit()

    # create boolean array to fill the array with all the sub-totals from the subsets
    # initialize all subsets to false
    # note: sub-totals will be true when they have reached the total value
    subset = [False] * (total + 1)
    # set totals at index 0 to true
    subset[0] = True

    # address base case (there's only one element, and the element is equivalent to total)
    if (n_items == 1 and list_items[0] == total):
        return True

    # fill in boolean array
    sub_total = 0
    while not subset[total] and sub_total < len( list_items ):
      a = list_items[sub_total]
      q = total
      while not subset[total] and q >= a:
        if not subset[q] and subset[q - a]:
          subset[q] = True
        q -= 1
      sub_total += 1
    # print result
    print(subset[total])
    sys.exit()

primePantry(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
