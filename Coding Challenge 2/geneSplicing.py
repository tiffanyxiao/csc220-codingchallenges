'''
Author: Tiffany Xiao
Collaborators: Karen Santamaria and Heidi
Date: February 13, 2018
Title: Gene Splicing

Objective: given two strings representing snippets of genes (letters ACGT), identify
the shortest string that could contain them both as subsequences.

Examples:
********************************************
string 1 – AACCTGT     string 2 – CTGTACG
shortest string that has both as substring
AACCTGTACG (length 10)
********************************************

Description:

To do:
-return all possible substrings of equal length
-remove test strings
'''

def get_overlap(string1, string2, len_string1, len_string2):
    '''Function to find the string that contains both strings.

    Parameters:
    string1 - first string inputted by user
    string2 - second string inputted by user
    len_string1 - length of string1
    len_string2 - length of string2

    Return:
    Returns the shortest string that has both as substring
    '''
    # automatic case if the strings are the same, return the string
    if (string1 == string2):
        return [string1]

    #string1 is associated with horizontal diraction
    #string2 is associated with vertical direction
    #everything initially filled in with 0's
    matrix = [[0 for col in range(len_string1)] for row in range(len_string2)]

    #fill in 1's with matches
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if (string1[col] == string2[row]):
                matrix[row][col] = 1

    #for every cell in the matrix, add the value of the upper-reight cell to the current cell
    #so the value of the cells will be the number of cosecutive match if there is any
    overlap_len = 0
    overlap_position = []
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if matrix[row][col] == 1 and row!=0 and col!=0:
                matrix[row][col] = matrix[row][col] + matrix[row-1][col-1]
                if matrix[row][col]>overlap_len:
                    overlap_len = matrix[row][col]
                    overlap_position = [row,col]

    large_share = 0
    large_share_pos = []

    for i in range(len(matrix)):
        if (large_share < matrix[i][len_string1-1]):
            current_pos = [i, len_string1-1]
            keep_going = True

            while (current_pos[0] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (matrix[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False

            if (keep_going):
                large_share = matrix[i][len_string1-1]
                large_share_pos = [i,len_string1-1]

    for i in range(len(matrix[len_string2-1])):
        if(large_share < matrix[len_string2-1][i]):
            current_pos = [len_string2-1,i]
            keep_going = True
            while(current_pos[1] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (matrix[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False
            if (keep_going):
                large_share = matrix[len_string2-1][i]
                large_share_pos = [len_string2-1, i]

    for item in matrix:
        print(item)

    print("largest shared positon", large_share_pos)
    print("largest sharted size", large_share)

    #construct the substring
    # if the largest shared size == 0
    if (large_share == 0):
        return [string1 + string2, string2 + string1]
    # if string is substring of another
    elif (large_share == len(string1)):
        return [string2]
    elif (large_share == len(string2)):
        return [string1]
    # if string is somewhere inbetween (either in front or in middle)
    elif (large_share_pos[1]+1 == len(string2)):
        return[string1+string2]
    elif (large_share_pos[0]+1 == len(string1)):
        return[string2+string1]

def main():
    '''Function asks user to input two strings (two gene sequences), then calls other functions to get the overlap of the strings
    and print it properly'''

    # list of all valid letters in gene sequence
    gene_list = ["A","C","T","G"]

    # intialize string1 and string2 (delete later)
    string1 = "AAA"
    string2 = "BAAAB"

    # # check string inputs
    # string1 = input("Input the first sequence" + "\n").upper()
    # for l in string1:
    #     if (l not in gene_list):
    #         raise ValueError('String1 is not a gene')
    #
    # string2 = input("Input the second sequence" + "\n").upper()
    # for l in string2:
    #     if (l not in gene_list):
    #         raise ValueError('String2 is not a gene')
    # create substring by generating overlap with strings
    union_result = get_overlap(string1,string2, len(string1), len(string2))
    # print in desired format
    print("**************************************")
    print("String 1 -", string1)
    print("String 2 -", string2)
    print("shortest string that has both as substring")
    for union in union_result:
        print(union, "(length " + str(len(union)) + ")")
    print("**************************************")

main()
