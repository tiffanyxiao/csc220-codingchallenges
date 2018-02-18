'''
Author: Tiffany Xiao
Date: February 8, 2018
Title: Redundancy Detector

Objective of challenge:
use dynamic programming to efficiently solve the following riddle:
**********************************************************
Given a positive integer n, you can perform any one of the
following 3 steps:
1. Subtract 1.
2. If n is divisible by 2, divide by 2.
3. If n is divisible by 3, divide by 3.
What is the minimum number of steps that takes n to 1?
**********************************************************

Output expected:


Description:

Todo:
-Try/catch for invalid inputs

'''

def dp_steps(n, knownResults):
    ''' Function to compute minimum number of steps
    Parameters:
    n - positive integer n (to calculate number of steps for)
    knownResults - previously calculated steps
    '''
    # Loop over all values, in order
    for num in range(1, n+1):
        # Worst case: subtract 1 constantly already addressed in beginning

        # initialize minimum number of steps
        minStep = 0

        # Calculate number of steps
        while(num != 1):
            # Check if it can be divided by 3
            if num%3==0:
                num = (num/3)
            elif num%2==0:
                num = (num/2)
            else:
                num -= 1
            minStep += 1
        knownResults[num-1] = minStep
    print knownResults

def main():
    # get user input for the interger n
    n = int(raw_input("Please input a positive integer"))

    knownResults = [n] * n

    dp_steps(n,knownResults)

    # test = dp_steps([1,2,3],n,knownResults)
    # print(test)


main()
