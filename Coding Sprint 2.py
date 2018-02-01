'''
Author: Tiffany Xiao
Date: January 30, 2018
Title: I Need a Little Validation

Objective of challenge:
Write a Contact class that stores the following:
name, phone number, email address
and checks to make sure that the
phone number and email address are valid

Description:
This program completes the objective of the challenge
by addressing a couple of cases for each attribute
of the class (name, phone number and email address).
It mandates the user to change invalid inputs for an
attribute until it is valid.
The program also allows the user to add multiple contacts.
I have added an additional function, error(), in order to
check the user input when prompting the user for adding
more contacts.
After adding all contacts, the program will print all the
contacts. I have included an additional function in the
Contact class to print all the attributes.

'''

class Contact():
    '''Class that stores a name, phone number, email address, with check and print functions'''

    def __init__(self, name, phoneNumber, emailAddress):
        self.name = name
        self.check_name()
        self.phoneNumber = phoneNumber
        self.check_phoneNumber()
        self.emailAddress = emailAddress
        self.check_emailAddress()

    # function to check name format
    def check_name(self):

        # binary value to keep track if the name is valid
        check = True

        # ask for a name in the valid format until it is valid
        while(check):
            # if there is no input
            if not self.name:
                check = True
            # if user only enters one space
            elif self.name == " ":
                self.name = True
            # break out of while loop
            else:
                check = False
            # prompt user for proper response
            if check == True:
                self.name = raw_input("Invalid name format. Try again (type something [make sure its not just a space]): ")

    # function to check phone number format
    def check_phoneNumber(self):
        # binary value to keep track if the phone number is valid
        check = True

        # ask for an phone number in the valid format until it is valid
        while(check):
            # if there is no input
            if not self.phoneNumber:
                check = True
            # if there are too many numbers
            elif len(self.phoneNumber) != 12:
                check = True
            # if the dashes are missing or misplaced
            elif (self.phoneNumber[3] != "-" and self.phoneNumber[7] != "-"):
                check = True
            # break out of while loop
            else:
                check = False
            # prompt user for proper response
            if check == True:
                self.phoneNumber = raw_input("Invalid phone number format. Try again (format: 123-456-7810): ")

    # function to check email address format
    def check_emailAddress(self):
        # binary value to keep track if the email address is valid
        check = True

        # ask for an email in the valid format until it is valid
        while(check):
            # if there is no input
            if not self.emailAddress:
                check = True
            # if @ or . is missing from the email address
            elif ("@" not in self.emailAddress) or ("." not in self.emailAddress):
                check = True
            #
            elif (self.emailAddress[0] == "@") or (self.emailAddress[len(self.emailAddress)-1] == "@"):
                check = True
            elif (self.emailAddress[0] == ".") or (self.emailAddress[len(self.emailAddress)-1] == "."):
                check = True
            # break out of while loop
            else:
                check = False
            # prompt user for proper response
            if check == True:
                self.emailAddress = raw_input("Invalid email format. Try again (format: ____@___.com): ")

    # function to print contact attributes
    def contact_print(self):
        print(self.name)
        print(self.phoneNumber)
        print(self.emailAddress)

def error(addContact):
    ''' Function to print error message when there is an invalid user input (not a 'Y' or 'N')'''
    response = raw_input("Error. Invalid input. Try again? Type 'Y' for yes and 'N' for no. \n")
    if response == "Y":
        addContact = True
        return addContact
    elif response == "N":
        addContact = False
        return addContact
    else:
        error(addContact)

def main():
    ''' Main function that asks user for contact information and checks inputs'''
    # print message to user with instructions
    print("Hello user! Welcome to your tiffPhone! \nLet's put some contacts in your tiffPhone.")

    # create a list to store all contacts
    contacts = []

    # binary value to decide whether or not to continue adding contacts
    addContact = True

    # while loop to continue adding contacts until user decides not to
    while(addContact):
        # ask user for contact attributes
        name = raw_input("What's the contact's name? ")
        phoneNumber = raw_input("What's the contact's phone number? (Please use 123-456-7890 format) ")
        emailAddress = raw_input("What's the contact's email address? ")

        # create instance of Contact class using attributes
        person = Contact(name, phoneNumber, emailAddress)

        # add contact to list of contacts
        contacts.append(person)

        # ask user if they'd like to continue adding contacts
        response = raw_input("Would you like to continue adding contacts? (Enter 'Y' for Yes and 'N' for No) ")
        if response == "Y":
            addContact = True
        elif response == "N":
            addContact = False
        else:
            # allow the user to edit their response
            addContact = error(addContact)

    # print all contacts and their contact information
    print("----------------------------------------------------------")
    print("Congratulations! Now you have contacts! \nHere are your contacts:")
    for i in range(len(contacts)):
        print(" ")
        print("Contact #"+str(i+1))
        contacts[i].contact_print()

main()
