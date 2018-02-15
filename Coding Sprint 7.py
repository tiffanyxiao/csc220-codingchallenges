'''
Author: Tiffany Xiao
Date: January 25, 2018

Objective of challenge:
Given a sequence of (integer, positive-valued) item weights,
identify whether or not there is a subset that could fill a
Prime Pantry Box to exactly 100%

Auther notes:
'''
def primePantry(boxes, n_items, total):
    all_pantries = []
    for box in boxes:
        one_pantry = [box]
        weight = boxes.get(box)
        print(weight)
        for otherbox in boxes:
            if (weight + boxes.get(otherbox) < total):
                one_pantry.append(otherbox)
                weight += boxes.get(otherbox)
        all_pantries.append(one_pantry)


    return all_pantries

def 

def main():
    primeComplete = primePantry({"pepsi":55, "detergent":30, "chips":25, "cereal":15}, 4, 100)
    print(primeComplete)

main()
