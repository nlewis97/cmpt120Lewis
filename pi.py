# Introduction to Programming
# Author: Nicholas Lewis
# Date: 2/5/18

# pi.py
# A program that serves as a calculator for pi.
import math
def picalculator():
    n = int(input("enter the numbers of terms to use:"))
    pi = 0
    sign = 1
    for i in range(1, n * 2 + 1, 2):
        term = (4/i*sign)
        pi = pi + term
        sign = sign*-1
    print("the approximate value of pi is", pi)
    subtract = (math.pi - pi)
    print ("The difference between the value of pi and the approximate value is", subtract)
    
picalculator()

    
