# Introduction to Programming
# Author: Nicholas Lewis
#Date: 4/27/18

#Tennisplayer.py
from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winstheServe(self):
        
        return random() <= self.prob

    def increaseScore(self):
        
        if self.score == 0:
            self.score = self.score + 15
        elif self.score == 15:
            self.score = self.score + 15
        elif self.score == 30:
            self.score = self.score + 10
        elif self.score == 40:
            self.score = self.score + 10

    def Score(self):
        
        return self.score
