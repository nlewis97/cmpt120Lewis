# Author: Nicholas Lewis
# Date: 4/13/2018
# ArithmeticEngine.py

from random import random

 

def main():

    print("Please pick one of the following actions: reward, punish, threaten, joke.")
    aifeelings = ["angry", "disgusted", "fearful", "happy", "sad", "suprised"]
    aiEmotionalstatus = int(random() * 6);
    #table for searching emotion
    C = [[2,0,4,3,4,3],[3,0,2,5,4,4],[0,1,2,1,4,2],[1,0,5,3,4,3],[2,0,1,5,4,4], [5,1,2,3,4,4]]

   

    def aiinteraction():

        action = input('I am currently feeling ' + aifeelings[aiEmotionalstatus] + ': ')
        if action.lower() == "threaten":
            return 0
        elif action.lower() == "reward":
            return 1
        elif action.lower() == "punish":
            return 2
        elif action.lower() == "joke":
            return 3
        else:
            return -1

       

    def findEmotion(currEmotionalstatus, inputAction):
        return C[inputAction][currEmotionalstatus]

 

    while True:
        feedback = aiinteraction()
        if feedback != -1:
            aiEmotionalstatus = findEmotion(aiEmotionalstatus, feedback)
        else:
            print("This is not a command.")

 

main()
