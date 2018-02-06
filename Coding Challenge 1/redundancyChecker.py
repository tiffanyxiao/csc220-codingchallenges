'''
Author: Tiffany Xiao
Collaborators: Karen Santamaria and Quynh Mai
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

To fix:
-Line numbers (currently counting line numbers after strip)
-reducing garbage & improving efficiency
-close files
-test against .py, .txt and .csv
-remove test path
'''
import glob, os
from itertools import combinations

def compare(file1, file2):
    """ Function to compare two files and identify a matching line, then print the matching lines in desired format.

    Parameters:
    file1 - the first file to check
    file2 - the second file to check
    """
    duplicate_found = False
    duplicate_count = 0
    ending = ""
    # create a dictionary using file1 and file2
    with open(file1) as file:
        lines = [line.strip() for line in file]
    a = dict((lines[i], i) for i in range(len(lines)))
    with open(file2) as file:
        lines2 = [line.strip() for line in file]
    b = dict((lines2[i], i) for i in range(len(lines2)))
    # find the intersection of the dictionaries (matching keys) and make a Pair object with the intersections
    for key in a.keys():
        if key in b.keys():
            duplicate_found = True
            duplicate_count += 1
            ending += "*** " + str(a[key]) + " "+  str(b[key]) + " " + key + "\n"

    # print file and matches only if a duplicate has been found
    if (duplicate_found):
        print("-------------------------------------")
        print("File 1: ", file1)
        print("File 2: ", file2)
        print("Number of identical lines: ", duplicate_count)
        print("-------------------------------------")
        print(ending)

def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    # ask user for path
    #path = raw_input("Please indicate path to directory below: \n")
    # test path: path '/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"
    path = "/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"

    # create a try catch block in case of invalid directory inputted
    try:
        # identify all python files in directory
        text_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        # get all combinations of text_files
        comb = combinations(text_files, 2) # currently only makes combinations with .py files

        # compare each combination of text files
        for i in list(comb):
            compare(i[0], i[1])

    except OSError:
        print("Invalid path to directory inputted. Please try again.")
        main()

main()
