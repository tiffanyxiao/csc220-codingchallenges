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
-removing the class to improve efficiency (print pair directly)
-create try & catch block for user input
'''
import glob, os
from itertools import combinations

class Pair():
    """ Class that is a pair object (a pair has two text file names, the matching line and the number of the line for both files) """

    def __init__(self, file1, file2, line, file1_num, file2_num):
        """ initialize a pair object.

        Parameters:
        file1 - the first file inputted
        file2 - the second file inputted
        line - the matching line identified in both files
        file1_num - the line number of the matching line in file 1
        file2_num - the line number of the matching line in file 2
        """
        self.file1 = file1
        self.file2 = file2
        self.line = line
        self.file1_num = file1_num
        self.file2_num = file2_num

def compare(file1, file2):
    """ Function to compare two files and identify a matching line

    Parameters:
    file1 - the first file to check
    file2 - the second file to check

    Returns a list of all the pairs (instances of the Pair class) generated from the two files
    """
    pairs = []
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
            pair = Pair(file1, file2, key, a.get(key), b.get(key))
            pairs.append(pair)
    return pairs

def printPairs(pairs):
    ''' Function takes in a list of pairs between two files, and prints the pair in desired output

    Parameters:
    pairs - a list of pairs
    '''
    print("-------------------------------------")
    print("File 1: ", pairs[0].file1)
    print("File 2: ", pairs[0].file2)
    print("Number of identical lines: ", len(pairs))
    print("-------------------------------------")
    for pair in pairs:
        print("*** ", pair.file1_num, pair.file2_num, pair.line)

def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    # ask user for path
    # path = raw_input("Please indicate path to directory below: \n")
    # test path: path '/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"
    path = "/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"

    # identify all python files in directory
    text_files = [f for f in os.listdir(path)]

    # get all combinations of text_files
    comb = combinations(text_files, 2) # currently only makes combinations with .py files

    all_pairs = []

    for i in list(comb):
        all_pairs.append(compare(i[0], i[1]))

    for pairs in all_pairs:
        if pairs:
            printPairs(pairs)

main()
