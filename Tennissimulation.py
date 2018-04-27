# Introduction to Programming
# Author: Nicholas Lewis
#Date: 4/27/18

# Tennissimulation.py
from simstats import SimStats
from Tennismatch import Tennismatch

def ProgIntro():
    print("This program functions as a simulation for a tennis match ")

def getStats():
    probA = float(input("Enter the probability of A winning: "))
    probB = float(input("Enter the probability of B winning: "))
    n = int(input("Enter the amount of games to simulate: "))
    return probA, probB, n
    
def main():
    ProgIntro()
    probA, probB, n = getStats()
    stats = SimStats()
    for i in range(n):
        thesim = Tennismatch(probA, probB)
        thesim.match()
        stats.update(thesim)
    stats.printReport()

main()
