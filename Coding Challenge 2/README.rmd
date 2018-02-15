# Gene Splicing
Objective of Program: Given two strings representing snippets of genes (letters ACGT), identify the shortest string that could contain them both as subsequences.

## How to Run:
1. Run python program "geneSplicing.py" with command "python" in terminal (note: we are using python 3.6.3)
2. Input genes as directed by program.

## Python Version
Python 3.6.3

## Efficiency
The program is more efficient than the recursive solution because it implements dynamic programming in that it builds up on previous knowledge. In the program, it does this by building a 2-d array that identifies matching characters, and uses previous matches to identify the longest matching string.

## Project Collaborators:
Tiffany Xiao, Karen Santamaria, Heidi Tsang

### Note:
The project can be found on [Github](https://github.com/tiffanyxiao/csc220-codingchallenges/blob/master/Coding%20Challenge%202/geneSplicing.py).
