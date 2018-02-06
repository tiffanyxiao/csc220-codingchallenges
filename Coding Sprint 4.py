'''
Author: Tiffany Xiao
Date: February 6, 2018
Title: Log Jammin'

Objective of challenge:
write a @printdebugger decorator that logs the enter/exit of a function
#nextlevel1: also log the parameters passed into the function
#nextlevel2: indent to show functions that were called from within other functions

Description:
This program completes the main objective and the next two levels. It is a simple
program that tests two functions.
'''

# Define 'printdebugger' wrapper
def printdebugger(func):
    # Define 'printdebug_and_call' Function
    def printdebugger_and_call(*args, **kwargs):
        printdebugger.calls += 1
        print("    "*(printdebugger.calls-1)+"+ Start of "+func.__name__)
        print("    "*(printdebugger.calls-1)+"Parameters passed into "+func.__name__+": "),
        for arg in args:
            print(arg),
        print("")
        print("    "*(printdebugger.calls-1) + "Function output (if any):"),
        func(*args)
        print("    "*(printdebugger.calls-1)+"-End of "+func.__name__)
        printdebugger.calls -= 1
        return
    printdebugger.calls = 0
    return printdebugger_and_call

@printdebugger
def test1(parameter1, parameter2):
    print("My name is Tiffany!")

@printdebugger
def main():
    print("Hello World!")
    test1("test1","test2")

main()
