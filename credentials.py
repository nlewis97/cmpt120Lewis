# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Nicholas Lewis
# Created: 2018-02-23
def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first +"."+ last
    print("Your new usenrame is", uname)
    passwd = input("Create a new password: ")
    if len(passwd) >= 8:
        print("The force is strong in this one…")
        print("Account configured. Your new email address is", uname + "@marist.edu")
    elif len(passwd) <8:
        print("Fool of a Took! That password is feeble! Create one that is at least 8 characters.")
        passwd = input("Create a new password: ")
        if len(passwd) >=8:
                print ("This password is worthy enough.")
                print("Account configured. Your new email address is", uname + "@marist.edu")
   
main()
