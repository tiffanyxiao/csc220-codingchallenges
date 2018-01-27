'''
Author: Tiffany Xiao
Date: January 25, 2018

Objective of challenge:
Write a short program that takes in a string and
prints a well-formed banner to the command line
***********************
* <any length string> *
***********************


Auther notes:
In order to address the edge case in which the user input is longer than the terminal size (thus, causing a strange
looking "banner"), I will allow the user to input a limit for the number of characters for each line if they choose
to do so.
'''

def error():
    ''' function to print error message'''
    response = raw_input("Error. Invalid input. Try again? Type 'Y' for yes. \n")
    if response == 'Y':
        main()

def main():
    # get user input
    user_input = raw_input("Input string below: \n")

    # get length of user input
    len_input = len(user_input)

    try:
        # ask user how many characters should be on each line
        num_chars = eval(raw_input("How many characters should be on each line? Enter '0' if you'd like the full string to be on one line. \n "))

        # check if num_chars is less than 0
        # if num_chars is less than 0, print error
        if (num_chars < 0):
            error()
        # else, continue with printing banner
        else:
            # print full number of characters if input is 0
            if num_chars == 0:
                # number of stars in first and last line of banner
                num_stars = len_input + 4
                # print first line of banner
                print("*"*num_stars)
                # print second line of banner
                print("* "+user_input+" *")
                # print third line of banner
                print("*"*num_stars)
            # else split user input by number of characters indicated, and print
            else:
                # number of stars in first and last line of banner
                num_stars = num_chars + 4
                # print first line of banner
                print("*"*num_stars)
                # get number of splits possible
                num_splits =  int(len_input / num_chars)
                # print lines
                for i in range(num_splits):
                    print("* "+user_input[num_chars*i:num_chars*(i+1)]+" *")
                # check if there are any remaining characters that have not been printed
                if(num_splits*num_chars != len_input):
                    print("* "+user_input[num_splits*num_chars:len_input]+(" "*(num_chars-(len_input-(num_splits*num_chars)))+" *"))
                # print third line of banner
                print("*"*num_stars)


    except NameError:
        error()

main()
