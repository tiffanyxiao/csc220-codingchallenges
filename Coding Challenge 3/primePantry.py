'''
Author: Tiffany Xiao
Date: February 18, 2018

Objective of challenge:
Given a dictionary of items and their (integer, positive-valued) item weights, identify
whether or not there is a subset that could fill a Prime Pantry Box to exactly 100%% and
report which items are in the subset

Example function call:
primePantryV2({“pepsi”:55,“detergent”:30, “chips”:25, “cereal”:15}, 4, 100)

Desired output:
[“pepsi”, “detergent”, “cereal”]

You only need to return one correct match to get full credit. Bonus point if you can return all matches. Rubric forthcoming.

Auther notes:

To do:
'''
import sys
import ast

def prime_pantry(dictItems, nItems, total) :
    ''' Function identifies whether or not there is a subset that could fill a
    Prime Pantry Box to exactly 100%

    dictItems - list of all item weights (integer, positive valued)
    nItems - number of items in dictItems
    total - total/sum requested (100 in this challenge)
    '''
    # check for some cases in which we do not need to run the entire function
    if total < 0 or total > sum(dictItems.values()):
        print("False")
        sys.exit()

    # convert dictionary into list of lists for easier iterating through them
    dictList = []
    for key, value in dictItems.items():
        temp = [key,value]
        dictList.append(temp)

    # create boolean array to fill the array with all the sub-totals from the subsets
    # initialize all subsets to false
    # note: sub-totals will be true when they have reached the total value
    subset = []
    for i in range(total+1):
        sub_subset = [False,[]]
        subset.append(sub_subset)

    # set totals at index 0 to true
    subset[0][0] = True
    print(subset)

    # address base case (there's only one element, and the element is equivalent to total)
    if (nItems == 1 and dictList[0][1] == total) or total in dictList:
        print("True")
        sys.exit()

    # list all the sums between 0 and total, and try to find a subset for each sum until
    # we find a sum for x (or reach the end of the list of items)
    iterator = 0
    # continue to fill while we have not reached end of subset and iterator is not at end
    while not subset[total][0] and iterator < len( dictList ):
        currentItem = dictList[iterator][1]
        currentPos = total
        # try to find a subset for the currentPos
        while not subset[total][0] and currentPos >= currentItem:
            if not subset[currentPos][0] and subset[currentPos - currentItem][0]:
                subset[currentPos][1].append(currentPos)
                subset[currentPos][1].append(currentPos-currentItem)
                subset[currentPos][0] = True
            currentPos -= 1
        print(subset[currentPos+1][1])
        iterator += 1
        print(subset)

    # print result
    print(subset[total][0])
    sys.exit()

prime_pantry(ast.literal_eval(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
