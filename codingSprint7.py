'''
Author: Tiffany Xiao
Date: February 15, 2018

Objective of challenge:
Given a sequence of (integer, positive-valued) item weights,
identify whether or not there is a subset that could fill a
Prime Pantry Box to exactly 100%

How your function should run:
primePantry(list, n_items, total)
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
    if (n_items == 1 and list_items[0] == total) or total in list_items:
        print("True")
        sys.exit()

    # list all the sums between 0 and total, and try to find a subset for each sum until
    # we find a sum for x (or reach the end of the list of items)
    iterator = 0
    # continue to fill while we have not reached end of subset and iterator is not at end
    while not subset[total] and iterator < len( list_items ):
        current_item = list_items[iterator]
        current_pos = total
        # try to find a subset for the current_pos
        while not subset[total] and current_pos >= current_item:
            if not subset[current_pos] and subset[current_pos - current_item]:
                subset[current_pos] = True
            current_pos -= 1
        print(subset)
        iterator += 1

    # print result
    print(subset[total])
    sys.exit()

primePantry(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
