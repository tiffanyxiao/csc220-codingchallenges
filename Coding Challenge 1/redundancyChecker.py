'''
Author: Tiffany Xiao
Collaborators: Karen Santamaria and Quynh Mai
Date: February 1, 2018
Title: Redundancy Detector

Objective of challenge:
write a program that reads all the files in a specified directory and prints a report of the lines that are identical
in any pair of files

Output expected:
-------------------------------------
File 1: <f1>
File 2: <f2>
Number of identical lines: <n>
-------------------------------------
*** <line_num_f1> < line_num_f2> <line_contents>
*** <line_num_f1> < line_num_f2> <line_contents>

Description:
The program consists of two functions - compare and main. main() will ask the user for the path to the specified directory.
Then, it will utilize tools from the combinations library to create unique combinations of files to check (to reduce time).
Next, it will loop through each combination and call compare() on each combination. compare() will check for identical lines
in the file. It will strip all files of whitespace and blanks lines, and put all lines with characters in them into a
dictionary with their line number. To check for identical lines, compare() will check the keys of each dictionary and check
for matches. Finally, it will print the results (if a match is found) as desired.

To fix:
-test against .py, .txt and .csv
-remove test path
-fix problem w/ duplicate lines not being detected
'''
import glob, os
from itertools import combinations

def compare(path, file1, file2):
    """ Function to compare two files and identify a matching line, then print the matching lines in desired format.

    Parameters:
    path - path to the files
    file1 - the first file to check
    file2 - the second file to check
    """
    # count number of duplicate lines
    duplicateCount = 0

    # string with all duplicate lines (and their line numbers)
    stringEnd = ""

    with open(path+"/"+file1) as file:
        lines = [line for line in file]
    a = [[lines[i].strip(), i+1] for i in range(len(lines)) if lines[i].strip()]

    with open(path+"/"+file2) as file:
        lines2 = [line for line in file]
    b = [[lines2[i].strip(), i+1] for i in range(len(lines2)) if lines2[i].strip()]

    for word_line in a:
        for word_line2 in b:
            if word_line[0] == word_line2[0]:
                duplicateCount += 1
                stringEnd += "*** " + str(word_line[1]) + " "+  str(word_line2[1]) + " " + word_line[0] + "\n"

    if (duplicateCount != 0):
        print("-------------------------------------")
        print("File 1: ", file1)
        print("File 2: ", file2)
        print("Number of identical lines: ", duplicateCount)
        print("-------------------------------------")
        print(stringEnd)

def main():
    ''' Function that asks user for a directory, then identifies all files in the directory, creates all possible
    unique file combinations, and then calls compare function on all the combinations.'''

    # ask user for path
    #path = raw_input("Please indicate path to directory below: \n")
    # test path: path '/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"
    path = "/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1/Tests"

    # create a try catch block in case of invalid directory inputted
    try:
        # identify all python files in directory
        textFiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        # get all combinations of textFiles
        comb = combinations(textFiles, 2)

        # compare each combination of text files
        for i in list(comb):
            compare(path, i[0], i[1])

    except OSError:
        print("Invalid path to directory inputted. Please try again.")
        main()

main()
