# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Nicholas Lewis
# Created: 2018-02-23
def firstName():
    first = input("Enter your first name: ")
    return(first)
def lastName():
    last = input("Enter your last name: ")
    return(last)
# JA: You are missing the function to check for the strenght of the password.
def uname():
    for i in range(5):
        firstN=firstName();
        lastN=lastName();
        uname = firstN + "." + lastN
        print("Your new usenrame is", uname.lower())
        passwd = input("Create a new password: ")
        if len(passwd) >= 8 and passwd.isupper:
            print("The force is strong in this one…")
            print("Account configured. Your new email address is", uname + "@marist.edu")
        if len(passwd) <8 or passwd.islower:
            print("Fool of a Took! That password is feeble! It is encouraged that you make a password at least 8 characters long and has at least one uppercase letter.")
            passwd = input("Create a new password: ")
            if len(passwd) >=8:
                print ("This password is worthy enough.")
                print("Account configured. Your new email address is", uname + "@marist.edu")
   
uname()
