'''
Author: Tiffany Xiao
Date: February 15, 2018

Objective of challenge:
Given a sequence of (integer, positive-valued) item weights,
identify whether or not there is a subset that could fill a
Prime Pantry Box to exactly 100%

How your function should run:
prime_pantry(list, nItems, total)
'''
import sys

def prime_pantry(listItems, nItems, total) :
    ''' Function identifies whether or not there is a subset that could fill a
    Prime Pantry Box to exactly 100%

    listItems - list of all item weights (integer, positive valued)
    nItems - number of items in listItems
    total - total/sum requested (100 in this challenge)
    '''
    # create list of ints with listItems
    listItems = [int(i) for i in listItems.strip('[]').split(',')]

    # check for some cases in which we do not need to run the entire function
    if total < 0 or total > sum(listItems):
        print("False")
        sys.exit()

    # create boolean array to fill the array with all the sub-totals from the subsets
    # initialize all subsets to false
    # note: sub-totals will be true when they have reached the total value
    subset = [False] * (total + 1)
    # set totals at index 0 to true
    subset[0] = True

    # address base case (there's only one element, and the element is equivalent to total)
    if (nItems == 1 and listItems[0] == total) or total in listItems:
        print("True")
        sys.exit()

    # list all the sums between 0 and total, and try to find a subset for each sum until
    # we find a sum for x (or reach the end of the list of items)
    iterator = 0
    # continue to fill while we have not reached end of subset and iterator is not at end
    while not subset[total] and iterator < len( listItems ):
        currentItem = listItems[iterator]
        currentPos = total
        # try to find a subset for the currentPos
        while not subset[total] and currentPos >= currentItem:
            if not subset[currentPos] and subset[currentPos - currentItem]:
                subset[currentPos] = True
            currentPos -= 1
        iterator += 1

    # print result
    print(subset[total])
    sys.exit()

prime_pantry(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
