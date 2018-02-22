'''
Author: Tiffany Xiao
Collaborator: Karen Santamaria
Date: February 18, 2018

Objective of challenge:
Given a dictionary of items and their (integer, positive-valued) item weights, identify
whether or not there is a subset that could fill a Prime Pantry Box to exactly 100%% and
report which items are in the subset

Example function call:
primePantryV2({“pepsi”:55,“detergent”:30, “chips”:25, “cereal”:15}, 4, 100)

Desired output:
[“pepsi”, “detergent”, “cereal”]
'''

import sys
import ast

def prime_pantry(dictItems, nItems, total) :
    ''' Function identifies whether or not there is a subset that could fill a
    Prime Pantry Box to exactly 100%, or the closest-without-going-over total

    Parameters:
    dictItems - dictionary of all items and their weights
    nItems - number of items in dictItems
    total - total/sum requested (100 in this challenge)
    '''
     # number of items and total to add must be >0
    if not(nItems > 0)  or not(total > 0):
        raise Exception("Number of items and total must be greater than 0.")

    # convert dictionary into list of lists to easily iterate through
    dictList = []
    for key, value in dictItems.items():
        temp = [key,value]
        # check if key and value of dictionary is valid
        if(not isinstance(key, str)):
            raise Exception('All item names must be strings.')
        if(not isinstance(value, int)):
            raise Exception('All item weights must be integers.')
        if(value <= 0):
            #all weights must be >0
            raise Exception('Weight of one of the items is less than or equal to 0.')
        dictList.append(temp)

    # create 2-d array to fill the array with all the sub-totals from the subsets
    # and the subset that creates the sub-total
    # initialize all subsets to a list with false and an empty list
    allSubset = [[False, []] for i in range(total+1)]

    # set total at index 0 to true, and append 0 the subset
    allSubset[0][0] = True
    allSubset[0][1].append(0)

    # address base case (there's only one element, and the element is equivalent to total)
    if (nItems == 1 and dictList[0][1] == total) or total in dictList:
        print("True")
        return

    # list all the sums between 0 and total, and try to find a subset for each sum until
    # we find a sum for x (or reach the end of the list of items)
    iterator = 0
    # continue to fill while we have not reached end of subset and iterator is not at end
    while not allSubset[total][0] and iterator < len( dictList ):
        currentItem = dictList[iterator][1]
        currentPos = total
        # try to find a subset for the currentPos
        while not allSubset[total][0] and currentPos >= currentItem:
            if not allSubset[currentPos][0] and allSubset[currentPos - currentItem][0]:
                # append subset components to list
                allSubset[currentPos][1].append(currentPos-(currentPos - currentItem))
                allSubset[currentPos][1].extend(allSubset[currentPos-currentItem][1])
                allSubset[currentPos][0] = True
            currentPos -= 1
        iterator += 1

    # print in desired output format
    # initialize list that contains all items that make up the allSubset
    allItems = []
    # keep track of the "largest" total (either total or the without-going-over solution)
    largest = 0
    # if a subset exists for total, largest = total
    if (allSubset[total][0]):
        largest = total
    # else, look for the without-going-over solution
    else:
        print("There are no items that perfectly add up to", total)
        # find closest number that is true
        for i in range(len(allSubset)-1,0,-1):
            if allSubset[i][0]:
                largest = i
                break
        if (largest != 0):
            print("The closest-without-going-over solution is: total =", largest)
        # if largest is 0, then print that there are no items
        else:
            print("Unfortunately, there are no items for you ...")
            return
    # find items that match with the weights in our subset list
    numItems = 0
    for key, value in dictItems.items():
        if value in allSubset[largest][1]:
            numItems += 1
            if numItems == len(allSubset[largest][1]):
                break
            allItems.append(key)
    # print all items
    print("Number of Items: ", len(allItems))
    print(allItems)

    return

prime_pantry(ast.literal_eval(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
