'''
Author: Tiffany Xiao
Date: February 13, 2018
Title: codebreaker

Objective of challenge: The difficulty of factoring large prime numbers is a primary
component of many modern encryption systems. Given a list of integers, return the prime factorization
for each (including “PRIME” if the number is prime).

Examples:
********************************************
121 = 11 * 11
39 = PRIME
240 = 2 * 2 * 2 * 2 * 3 * 5
********************************************

Description:
This program utilizes multiprocessing to compute the prime factors of a list of integers inputted by the
user, and print as desired in the objective. 

'''
import multiprocessing as mp

def find_prime_facs(n):
    ''' Function that finds factors of a number, and then prints the number and its factors in desired format
    Parameters:
    n = integer to find factors of
    '''
    # if the number is less than 2, report that it's a "special case"
    if n < 2:
        print(n," = A SPECIAL NUMBER!")
        return
    # save the number
    number = n
    # create a list of the factors
    list_of_factors=[]
    # assign a number to keep track of index
    i=2
    # find all factors of the number
    while n>1:
        if n%i==0:
          list_of_factors.append(i)
          n=n/i
          i=i-1
        i+=1
    # print the factors in desired format
    print(number,"= ",end ='')
    if len(list_of_factors) != 1:                                       # print factors for NON PRIME
        for i in range(len(list_of_factors)):
            print(list_of_factors[i], end='')
            if i != len(list_of_factors)-1:                             # print * if it's not the last factor
                print( " * ", end='')
        print("")
    else:
        print("PRIME")


def main():
    ''' Function that asks user to input a list of integers, then computes
    the prime factorization of each with multiprocessing by calling find_prime_facs()'''
    # try catch block for invalid input exceptions
    try:
        # ask user for input
        integers = input("Please input integers (with space inbetween each integer): ").split()

        print("********************************************")           # formatting

        # utilize multiprocessing to print each integers' prime factorization
        pool = mp.Pool(processes = 4)
        results = [pool.apply(find_prime_facs, args=(eval(integer),))
               for integer in integers]

        print("********************************************")           # formatting
    except:
        print("Invalid input. Please try again.")
        main()

main()
