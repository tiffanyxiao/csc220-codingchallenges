# Redundancy Checker
Objective of Program: Write a program that reads all the files in a specified directory and prints a report of the lines that are identical in any pair of files.

## How to Run:
1. Run python program "redundancyChecker.py" with command "python" in terminal (note: we are using python 2.7.10)
2. Input path to the directory you would like to check.

## Python Version
Python 2.7.10

## Edge Cases Addressed:
* User inputs invalid directory
* redundancyChecker.py is not in the path to check
* Lines are stripped of whitespace, so that two lines containing the same characters (minus the indentation at the beginning) are treated as the same line.
* Lines containing spaces (whitespace) do not count as lines to be matched

## TODO:
* test having 3 defs in one file and 1 def in 1 file (and vice versa)
* lines that begin with equivalent white space is not the same line?
* testing docstrings
* test other types of files

## Project Collaborators:
Tiffany Xiao, Karen Santamaria, Quynh Mai

### Note:
The project can be found on [Github](https://github.com/tiffanyxiao/csc220-codingchallenges/tree/master/Coding%20Challenge%201). On the Github page, there are test cases and an additional redundancyChecker.py that utilizes classes (our initial code without addressing certain edge cases).  
