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
def primePantry(boxes, n_items, total):
    all_pantries = []
    for box in boxes:
        one_pantry = [box]
        weight = box
        for otherbox in boxes:
            if (weight + otherbox <= total) and (otherbox not in one_pantry):
                one_pantry.append(otherbox)
                weight += otherbox
        if weight == 100:
            return True
    return False

def main():
    ''' Function to test primePantry function '''
    primeComplete = primePantry([55, 22, 30, 15], 4, 100)
    if primeComplete:
        print("True")

main()
