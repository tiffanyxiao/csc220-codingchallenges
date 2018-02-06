'''
Author: Tiffany Xiao
Date: February 6, 2018
Title: Log Jammin'

Objective of challenge:
write a @printdebugger decorator that logs the enter/exit of a function
#nextlevel1: also log the parameters passed into the function
#nextlevel2: indent to show functions that were called from within other functions

Description:
This program completes the main objective and the next two levels. It is a simple program that tests two functions.

Further works:
Perhaps implementing a calculator program would be a better way to test the program.
'''

def printdebugger(func):
    ''' Wrapper to print debugging statements before and after a function call. Also takes note of parameters '''

    def printdebugger_and_call(*args, **kwargs):
        # variable to track number of indents needed (times printdebugger is called)
        printdebugger.calls += 1

        print("    "*(printdebugger.calls-1)+"+Start of "+func.__name__)                       # print start statement

        # print args and kwargs only if there are parameters
        if (args) or (any(kwargs)):
            # print each parameter in args
            print("    "*(printdebugger.calls-1)+"Parameters passed into "+func.__name__+": "),
            for arg in args:
                print(arg),
            for key, value in kwargs.items():
                print ("(key: "+str(key)+", value: "+str(value)+")"),
            print("")

        print("    "*(printdebugger.calls-1) + "Function output (if any):"),                    # print function output
        func(*args, **kwargs)                                                                             # call function
        print("    "*(printdebugger.calls-1)+"-End of "+func.__name__)                          # print end statement
        # finished with this function, dedent
        printdebugger.calls -= 1
        return
    printdebugger.calls = 0
    return printdebugger_and_call

@printdebugger
def test2(**kwargs):
    ''' Function to test kwargs in debugger and does nothing with it (for testing) '''
    print("I love coding!")

@printdebugger
def test1(parameter1, parameter2):
    ''' Function that takes in two parameters and does nothing with it (for testing)'''
    print("My name is Tiffany!")

@printdebugger
def main():
    ''' Function prints string and then calls another function'''
    print("Hello World!")
    test1("test1","test2")

main()
test2(a = 5, b = 6, c = 7)
