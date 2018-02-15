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

def string_union(string1, string2,substring):
    '''make the shortest string  that contains string1 and string2 as subsequences'''
    union_result = ""
    if string1.endswith(substring):
        union_result = string1+ string2.replace(substring,"")
    else:
        union_result = string2+ string1.replace(substring,"")
    return union_result

def get_overlap(string1, string2, len_string1, len_string2):
    '''Function to find the string that contains both strings.

    Parameters:
    string1 - first string inputted by user
    string2 - second string inputted by user
    len_string1 - length of string1
    len_string2 - length of string2

    Return:
    Returns the overlap string
    '''
    # string1 and string2 form a 2D array where string1 is the horizontal direction and
    # string2 is the vertical direction

    # declare 2d array to store the values
    arrayValues = [[None]*(len_string2+1) for i in range(len_string1+1)]

    # build arrayValues from bottom up
    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0:
                arrayValues[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                arrayValues[i][j] = arrayValues[i-1][j-1]+1
            else:
                arrayValues[i][j] = max(arrayValues[i-1][j], arrayValues[i][j-1])

    # if the max is 0, then print error (for now)
    if arrayValues[len_string1][len_string2] == 0:
        print("error")
        return

    # last element of 2d array (arrayValues[len_string1][len_string2] should have the length of the smallest substring)
    # find the overlap position by using this number (find first instance of this number)
    overlap_position = []
    for k in range(len_string1+1):
        for l in range(len_string2+1):
            if arrayValues[k][l] == arrayValues[i][j]:
                overlap_position.append([k, l])

    # check that the first largest count is

    # identify which string contains the substring
    # if len_string1 == overlap_position[0] and len_string2 == overlap_position[1]:
    #     # perform substring on longer string
    # elif len_string1 == overlap_position[0]:
    #     # perform substring on string2
    # elif len_string2 == overlap_position[1]:
    #     #perform substring on string1


    #overlap_position = [[k,l] for k in range(len_string1+1) for l in range(len_string2+1) if arrayValues[k][l]==arrayValues[i][j] ]
    print(arrayValues[i][j])
    print(arrayValues)
    print(overlap_position)

    # #for every cell in the matrix, add the value of the upper-reight cell to the current cell
    # #so the value of the cells will be the number of consecutive match if there is any
    # overlap_len = 0
    # overlap_position = []
    # for col in range (0,len_string1):
    #     for row in range (0,len_string2):
    #         if matrix[row][col] == 1 and row!=0 and col!=0:
    #             matrix[row][col] = matrix[row][col] + matrix[row-1][col-1]
    #             if matrix[row][col]>overlap_len:
    #                 overlap_len = matrix[row][col]
    #                 overlap_position = [row,col]
    #
    # #construct the substring
    # if (overlap_position):
    #     overlap = string1[overlap_position[1]]
    #     for l in range(1, overlap_len):
    #         overlap = string1[overlap_position[1]-l]+overlap
    #
    # else:
    #     overlap = ""
    # return overlap


def main():
    '''Function asks user to input two strings (two gene sequences), then calls other functions to get the overlap of the strings
    and print it properly'''

    # list of all valid letters in gene sequence
    gene_list = ["A","C","T","G"]

    # intialize string1 and string2 (delete later)
    string1 = "AATCG"
    string2 = "GTTCG"

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
    substring = get_overlap(string1,string2, len(string1), len(string2))
    # get the union using substring result
    union_result = string_union(string1, string2, substring)
    # print in desired format
    print("**************************************")
    print("String 1 -", string1)
    print("String 2 -", string2)
    print("shortest string that has both as substring")
    print(union_result, "(" + str(len(union_result)) + ")")
    print("**************************************")

main()
