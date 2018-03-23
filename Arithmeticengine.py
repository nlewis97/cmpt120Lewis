# Author: Nicholas Lewis
# Date: 3/22/2018
# ArithmeticEngine.py

 

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()

        if cmd in ("sub", "add", "mult", "div"):
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
            except:
                print("An error has occured. Please try again.")

        if cmd == "add":
            result = num1 + num2
            print("The result is " + str(result) + ".\n")

        elif cmd == "sub":
            result = num1 - num2
            print("The result is " + str(result) + ".\n")

        elif cmd == "mult":
            result = num1 * num2
            print("The result is " + str(result) + ".\n")

        
        elif cmd == "div":
            if num2 == 0:
                print("Error: Cannot divide by zero. Please try again.")
                
            else:
                result = num1 // num2
                print("The result is " + str(result) + ".\n")
                
            
        elif cmd == "quit":
            break
        else:

            print("Sorry", cmd, "is not a valid command. Please try again.")

   

def main():
    showIntro()
    doLoop()
    showOutro()

main()
