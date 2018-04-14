# Introduction to Programming
# Author: Nicholas Lewis
#Date: 3/30/18


# Calculatorproject.py
# A program that uses graphics and buttons to create a functional calculator.
# Some improvements made to calculator.

# JA: When you switch the scientific mode, you should keep the other basic operations


from graphics import *


from button import Button
import math


 

class Calculator:
    def __init__(self):
        win = GraphWin("calculator")
        win.setCoords(0,0,16.5,21)   
        win.setBackground("black")
        self.win = win
        self.__createButtons()
        self.__createDisplay()
        self.AnswerDisplay()
        self.memorystorage()
        self.memory = "0"
#Memory functions now show up along the right side of display.
    def memorystorage(self):
        text = Text(Point(12,18.75),"")
        text.draw(self.win)
        text.setFace("courier")
        text.setSize(10)
        self.M = text
        
      
    def __createButtons(self):
        bSpecs = [(3.75,1.5,'0'), (6,1.5,'.'), (1.5,3.75,'1'), (3.75,3.75,'2'), (6,3.75,'3'),
                   (8.25,3.75,'+'), (10.5,3.75,'-'), (1.5,6,'4'), (3.75,6,'5'), (6,6,'6'),
                   (8.25,6,'*'), (10.5,6,'/'), (1.5,8.25,'7'), (3.75,8.25,'8'), (6,8.25,'9'),
                   (8.25,8.25,'<-'),(10.5,8.25,'C'), (12.75,1.5,'1/x'), (12.75,3.75,'%'),
                   (12.75,8.25,'sqrt'), (12.75,6,'x**2'), (3.75,15,'M+'), (6,15,'MS'),
                   (8.25,15,'MR'), (1.5,15,'MC'), (12.75,15,'sci')]
        self.buttons = []
        
        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),2.27,2.33,label))
        self.buttons.append(Button(self.win,Point(9.3,1.5),4.5,1.9,"="))
        for b in self.buttons:  b.activate()
#Operations for Sci mode
    def __SCI(self):
        bSpecs = bSpecs = [(3.75,1.5,'0'), (6,1.5,'.'), (1.5,3.75,'1'), (3.75,3.75,'2'), (6,3.75,'3'),
                   (8.25,3.75,'+'), (10.5,3.75,'-'), (1.5,6,'4'), (3.75,6,'5'), (6,6,'6'),
                   (8.25,6,'*'), (10.5,6,'/'), (1.5,8.25,'7'), (3.75,8.25,'8'), (6,8.25,'9'),
                   (8.25,8.25,'<-'),(10.5,8.25,'C'), (12.75,1.5,'1/x'), (12.75,3.75,'%'),
                   (12.75,8.25,'sqrt'), (12.75,6,'x**2'), (3.75,15,'M+'), (6,15,'MS'),
                   (8.25,15,'MR'), (1.5,15,'MC'), (1.5,10.5,'ln'), (1.5, 12.75,'log'),
                    (3.75,10.5,'x**y'), (15,8.5,'atan'), (15,6.5,'asin'), (15,4.00,'acos'), (6,10.5,'10^x'), (10.5,10.5,'sin'),
                (8.25,10.5 ,'cos'), (12.75,10.5,'tan'), (15,10.5,'('), (15,12.5,')')]
    
  
        self.buttons = []

        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),2.350,2.30,label))
        self.buttons.append(Button(self.win,Point(9.3,1.5),4.5,1.9,"="))
        for b in self.buttons:  b.activate()



    def __createDisplay(self):
        bg = Rectangle(Point(.75,18), Point(12.75,20))
        bg.setFill('pink')
        bg.draw(self.win)
        text = Text(Point(6.75,18.75), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.display = text
#This is another display where the answer will go.
    def AnswerDisplay(self):
        bg = Rectangle(Point(.75,16.5), Point(12.75,18))
        bg.setFill('pink')
        bg.draw(self.win)
        text = Text(Point(6.75,17.25), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.displayanswer = text

    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()
 

    def processButton(self, key):

        text = self.display.getText()

        if key == 'C':

            self.display.setText("")
            self.displayanswer.setText("")
        elif key == '<-':

            self.display.setText(text[:-1])

        elif key == '=':

            try:

                result = eval(text)

            except:

                result = 'ERROR'

            self.displayanswer.setText(str(result))

        else:

            self.display.setText(text+key)

            
        if key == 'MR':
            self.display.setText(self.memory)
            
        
        elif key == 'MS':
            self.memory = text or '0'
            if self.memory != '0':
                self.M.setText('M')
        elif key == 'M+':
            self.memory = str(eval(text+'+'+str(self.memory)))
            if self.memory != '0':
                self.M.setText('M+')
        elif key == 'MC':
            self.memory = "0"
            self.M.setText('')
        elif key == '1/x':
            try:
                result = 1/(eval(text))
            except:
                result = 'ERROR'
            self.displayanswer.setText(str(result))
        elif key == 'sqrt':
            result = (eval(text))**0.5
            self.displayanswer.setText(str(result))
            
        elif key == 'x**2':
            result = eval(text)**2
            self.displayanswer.setText(str(result))
        
      
        elif key == 'sqrt':
            result = (eval(text))**0.5
            self.displayanswer.setText(str(result))

        elif key == 'sci':
            self.__SCI()
            self.display.setText(text[-10:])

        elif key  == 'back':
            self.__createButtons()
            self.display.setText(text[-10:])

        elif key == 'ln':

            result = math.log(eval(text))
            self.displayanswer.setText(str(result))

        elif key == '10**x':

            result = (eval(text))
            self.displayanswer.setText(str(result))
            
        elif key == 'cos':
            result = math.cos(eval(text))
            self.displayanswer.setText(str(result))

        elif key == 'tan':
            result = math.tan(eval(text))
            self.displayanswer.setText(str(result))

        elif key == 'sin':
            result = math.sin(eval(text))
            self.displayanswer.setText(str(result))

        elif key == 'acos':
            result = math.acos(eval(text))
            self.displayanswer.setText(str(result))

        elif key == 'asin':
            result = math.asin(eval(text))
            self.displayanswer.setText(str(result))

        elif key == 'atan':
            result = math.atan(eval(text))
            self.displayanswer.setText(str(result))
        
        elif key == 'x**y':

            y = eval(input('Please Enter a Value for y:'))
            result = (eval(text))**y
            self.displayanswer.setText(str(result))
            
        elif key == 'log':
            result = math.log10(eval(text))
            self.displayanswer.setText(str(result))
 
        elif key == '10^x':
            result = 10**(eval(text))
            self.displayanswer.setText(str(result))
            
    def run(self):

        while True:

            key = self.getButton()

            self.processButton(key)

 
if __name__ == '__main__':
    tCalc = Calculator()
    tCalc.run()
Calculator()

   
