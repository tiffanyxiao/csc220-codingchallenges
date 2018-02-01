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
def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    # ask user for path
    path = raw_input("Please indicate path to directory below: \n")
    # test path: path = '/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges'

    # identify all python files in directory
    text_files = [f for f in os.listdir(path) if f.endswith('.py')]

    # binary value if identical lines are found
    identicalLine = False

    # only print this when
    while identicalLine = True:
        print("-------------------------------------")
        print("File 1: ")
        print("File 2: ")
        print("Number of identical lines: ")
        print("-------------------------------------")





    # print each file name and the number of lines in each file
    for text_file in text_files:
        print(text_file+" "+str(file_len(text_file)))

main()
