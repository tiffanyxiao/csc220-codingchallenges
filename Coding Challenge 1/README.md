# Gene Splicing
Objective of Program: Given two strings representing snippets of genes (letters ACGT), identify the shortest string that could contain them both as subsequences.

## How to Run:
1. Run python program "geneSplicing.py" with command "python" in terminal (note: we are using python 3.6.3)
2. Input genes as directed by program.

## Python Version
Python 3.6.3

## Efficiency
The program is efficient in a few ways:
1. To avoid redundancy when checking files, we generated unique combinations of files (i.e. the program treats (file1.py, file2.py) and (file2.py, file1.py) as one unique combination, and will only check this pairing of files for matches once).
2. We utilized list comprehensions multiple times throughout our program for more efficiency (i.e. when opening files and creating a list of lines and when creating 2d lists of stripped lines and line numbers).
3. To avoid iterating through blank lines, we stripped files of their blank lines.

## Edge Cases Addressed:
* User inputs invalid directory
* redundancyChecker.py is not in the path to check
* Lines are stripped of whitespace, so that two lines containing the same characters (minus the indentation at the beginning) are treated as the same line.
* Lines containing spaces (whitespace) do not count as lines to be matched
* Files that have repeated lines (i.e. file1 has 3 instances of "main" and file2 has 4 instances of "main") will output all matches.

## Project Collaborators:
Tiffany Xiao, Karen Santamaria, Heidi Tsang

### Note:
The project can be found on [Github](https://github.com/tiffanyxiao/csc220-codingchallenges/tree/master/Coding%20Challenge%201). On the Github page, there are test cases and an additional redundancyChecker.py that utilizes classes (our initial code without addressing certain edge cases).  
