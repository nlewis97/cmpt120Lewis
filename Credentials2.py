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
def uname():
    for i in range(5):
        firstN=firstName();
        lastN=lastName();
        uname = firstN + "." + lastN
        print("Your new username is", uname)
        passwd = input("Create a new password: ")
        if len(passwd) >= 8:
            print("The force is strong in this one…")
            print("Account configured. Your new email address is", uname + "@marist.edu")
        elif len(passwd) <8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
            if len(passwd) >=8:
                    print ("This password is worthy enough.")
                    print("Account configured. Your new email address is", uname + "@marist.edu")

    


uname()


