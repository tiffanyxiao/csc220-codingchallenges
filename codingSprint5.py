'''
Author: Tiffany Xiao
Date: February 8, 2018
Title: Minimum Steps to One

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
'''

def main():
    # get user input for the interger n
    num = int(input("Please input a positive integer: "))

    # create and initialize arrays storing output and result
    out = [num]*(num+1)

    # establish base case
    out[1] = 0;
    # go through each number in num and determine if they can be divide by 2 or 3
    for i in range(2, num+1, 1):
        out[i] = out[i-1] + 1
        if (i%2 == 0):
            out[i] = min(1 + out[int(i/2)], out[i])
        if (i%3 == 0):
            out[i] = min(1 + out[int(i/3)], out[i])

    print("The minimum number of steps to go down to 1 is: ", out[num])

main()
