'''
Author: Tiffany Xiao
Date: February 1, 2018
Title: Redundancy Detector

Objective of challenge:
write a program that reads all the files in a specified
directory and prints a report of the lines
that are identical in any pair of files

Output expected:
-------------------------------------
File 1: <f1>
File 2: <f2>
Number of identical lines: <n>
-------------------------------------
*** <line_num_f1> < line_num_f2> <line_contents>
*** <line_num_f1> < line_num_f2> <line_contents>

Description:
'''
import glob, os
from itertools import combinations

def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    # ask user for path
    #path = raw_input("Please indicate path to directory below: \n")
    # test path: path = '/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"
    path = "/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"

    # identify all python files in directory
    text_files = [f for f in os.listdir(path) if f.endswith('.py')]

    # get all combinations of text_files
    comb = combinations(text_files, 2) # currently only makes combinations with .py files

    for i in list(comb):
        print i



    # get two dictionary with line numbers as key and line as value
    with open("testfile1.py") as file:
        lines = [line.strip() for line in file]
    a = dict((lines[i], i) for i in range(len(lines)))
    with open("testfile2.py") as file:
        lines2 = [line.strip() for line in file]
    b = dict((lines2[i], i) for i in range(len(lines)))
    # find intersection of the dictionaries
    for key in a.keys():
        if key in b.keys():
            print("True")






    outfile = open('results.txt', 'wb')
    for i in b:
      print>>outfile, i
    outfile.close()

    '''x = set([i.strip() for i in open('testfile1.py')])
    y = set([i.strip() for i in open('testfile2.py')])
    z = x.intersection(y)
    outfile = open('results.txt', 'wb')
    for i in z:
      print>>outfile, i
    outfile.close()'''


    # binary value if identical lines are found
    '''identicalLine = False

    # only print this when
    while identicalLine = True:
        print("-------------------------------------")
        print("File 1: ")
        print("File 2: ")
        print("Number of identical lines: ")
        print("-------------------------------------")


    # print each file name and the number of lines in each file
    for text_file in text_files:
        print(text_file+" "+str(file_len(text_file)))'''

main()
