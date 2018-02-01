'''
Author: Tiffany Xiao
Date: February 1, 2018
Title: python-o-meter

Objective of challenge:
write a program that reads all the python files
in a specified directory and prints out
the number of lines of code in each
(ignoring whitespace and comments)
[User inputted directory]

'''
import glob, os

def file_len(fname):
    ''' Function that counts the number of non-blank lines in given file'''
    non_blank_count = 0

    with open(fname) as infp:
        for line in infp:
            # don't count whitespace and comments
            if line.strip() and not line.strip().startswith("#"):
                non_blank_count += 1

    return non_blank_count

def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    # ask user for path
    path = raw_input("Please indicate path to directory below: \n")
    # test path: path = '/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges'

    # identify all python files in directory
    text_files = [f for f in os.listdir(path) if f.endswith('.py')]

    # print each file name and the number of lines in each file
    for text_file in text_files:
        print(text_file+" "+str(file_len(text_file)))
main()
