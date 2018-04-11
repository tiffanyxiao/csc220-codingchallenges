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
'''

def get_overlap(string1, string2, len_string1, len_string2):
    '''Function to find the string that contains both strings. The function first builds a 2d array with string1
    and string2 (string1 is the columns, string2 is the rows) and identifies the maximum number of overlapping
    characters. The union/slicing of the strings is created by a group of conditionals that check the string
    positions and how it correlates with the maximum number of overlapping characters.

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
    # if string is substring of another
    elif (string1 in string2):
        return [string2]
    elif (string2 in string1):
        return [string1]

    # initialize array with values of 0
    arrayValues = [[0 for col in range(len_string1)] for row in range(len_string2)]

    #fill in 1's with matches
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if (string1[col] == string2[row]):
                arrayValues[row][col] = 1

    # for every cell in the arrayValues, add the value of the upper-reight cell to the current cell
    # so the value of the cells will be the number of cosecutive match if there is any
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if arrayValues[row][col] == 1 and row!=0 and col!=0:
                arrayValues[row][col] = arrayValues[row][col] + arrayValues[row-1][col-1]

    # keep track of the number of largest share (the largest number shared) && largest share position (the position
    # the number is stored at)
    large_share = 0
    large_share_pos = []


    #find the largest shared position in bottom row
    for i in range(len(arrayValues)):
        if (large_share < arrayValues[i][len_string1-1]):
            current_pos = [i, len_string1-1]
            keep_going = True

            #find if any zeros found while retracing
            while (current_pos[0] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (arrayValues[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False

            #if no zeros found update the largest substring information
            if (keep_going):
                if (large_share == arrayValues[i][len_string1-1]):
                    large_share_pos.append([i,len_string1-1])
                else:
                    large_share = arrayValues[i][len_string1-1]
                    large_share_pos = [[i,len_string1-1]]

    #find the largest shared position using the rightmost column
    for i in range(len(arrayValues[len_string2-1])):
        if(large_share <= arrayValues[len_string2-1][i]):
            current_pos = [len_string2-1,i]
            keep_going = True

            #find it any zeros are encountered retracing
            while(current_pos[1] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (arrayValues[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False

            #if no zeros found update the largest substring information
            if (keep_going):
                if (large_share == arrayValues[len_string2-1][i]):
                    large_share_pos.append([len_string2-1, i])
                else:
                    large_share = arrayValues[len_string2-1][i]
                    large_share_pos = [[len_string2-1, i]]

    union = []
    # construct the substring (the union)
    # if the largest shared size == 0
    if (large_share == 0):
        return [string1 + string2, string2 + string1]
    # # if string is somewhere inbetween (either in front or in middle)
    for share in large_share_pos:
        if (share[0]+1 == len_string2):
            union.append(string2 + string1[share[1]+1:])

        elif (share[1]+1 == len_string1):
            union.append(string1 + string2[share[0]+1:])

    return union

def main():
    '''Function asks user to input two strings (two gene sequences), then calls other functions to get the overlap of the strings
    and print it in desired format'''

    # list of all valid letters in gene sequence
    gene_list = ["A","C","T","G"]

    # check string inputs
    string1 = input("Input the first sequence" + "\n").upper()
    if not string1:
        raise ValueError('String1 is not a gene')
    for l in string1:
        if (l not in gene_list):
            raise ValueError('String1 is not a gene')

    string2 = input("Input the second sequence" + "\n").upper()
    if not string2:
        raise ValueError('String2 is not a gene')
    for l in string2:
        if (l not in gene_list):
            print(len(string2))
            raise ValueError('String2 is not a gene')
    #create substring by generating overlap with strings
    union_result = get_overlap(string1,string2, len(string1), len(string2))
    # print in desired format
    print("********************************************")
    print("string 1 -", string1, "    string 2 -", string2)
    print("shortest string that has both as substring")
    for union in union_result:
        print(union, "(length " + str(len(union)) + ")")
    print("********************************************")

main()
