# Introduction to Programming
# Author: Nicholas Lewis
# Date: 2/5/18

# fibonacci.py
# A program that serves as an interactive fibonacci calculator.

def fibonaccigenerator():
    n,z = 1,1
    num = eval(input("Enter the sequence number of the fibonacci number you would like calculated:"))
    num_int=int(num-2)
    for i in range(num_int):
        n,z=z,n+z
    print("This secuence number gives the fibonacci value of", z)
fibonaccigenerator()
          
