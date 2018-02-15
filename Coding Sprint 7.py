'''
Author: Tiffany Xiao
Date: January 25, 2018

Objective of challenge:
Given a sequence of (integer, positive-valued) item weights,
identify whether or not there is a subset that could fill a
Prime Pantry Box to exactly 100%

Auther notes:

To do:
-sort it
'''
import multiprocessing as mp

def primePantry(boxes, n_items, total):
    all_pantries = []
    for box in boxes:
        one_pantry = [box]
        weight = boxes.get(box)
        for otherbox in boxes:
            if (weight + boxes.get(otherbox) <= total) and (otherbox not in one_pantry):
                one_pantry.append(otherbox)
                weight += boxes.get(otherbox)
        if weight == 100:
            return True
    return False

def main():
    primeComplete = primePantry({"pepsi":55, "chips":25, "detergent":30, "cereal":15}, 4, 100)
    if primeComplete:
        print("True")

main()
