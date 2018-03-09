# Introduction to Programming
# Author: Nicholas Lewis
#Date: 2/23/18


# Calculatorproject.py
# A program that uses graphics and buttons to create a functional calculator.




from graphics import *

from button import Button

 

class Calculator:
    def __init__(self):
        win = GraphWin("calculator")
        win.setCoords(0,0,11,14.5)   
        win.setBackground("black")
        self.win = win
        self.__createButtons()
        self.__createDisplay()
      
    def __createButtons(self):
        bSpecs = [(2.5,1,'0'), (4,1,'.'), (1,2.5,'1'), (2.5,2.5,'2'), (4,2.5,'3'),
                   (5.5,2.5,'+'), (7,2.5,'-'), (1,4,'4'), (2.5,4,'5'), (4,4,'6'),
                   (5.5,4,'*'), (7,4,'/'), (1,5.5,'7'), (2.5,5.5,'8'), (4,5.5,'9'),
                   (5.5,5.5,'<-'),(7,5.5,'C'),(1,1,'OFF'), (8.5,1,'1/x'), (8.5,2.5,'%'),
                   (8.5,5.5,'sqrt'), (8.5,4,'x**2'), (2.5,10,'M+'), (4,10,'MS'),
                   (5.5,10,'MR'), (1,10,'MC')]
        self.buttons = []
        
        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,1.25,label))
        self.buttons.append(Button(self.win,Point(6.25,1),3,1.25,"="))
        for b in self.buttons:  b.activate()

 

    def __createDisplay(self):
        bg = Rectangle(Point(.5,12), Point(8.5,13))
        bg.setFill('pink')
        bg.draw(self.win)
        text = Text(Point(4.5,12.5), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.display = text


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

        elif key == '<-':

            self.display.setText(text[:-1])

        elif key == '=':

            try:

                result = eval(text)

            except:

                result = 'ERROR'

            self.display.setText(str(result))

        else:

            self.display.setText(text+key)

 

    def run(self):

        while True:

            key = self.getButton()

            self.processButton(key)

 

if __name__ == '__main__':

    theCalc = Calculator()

    theCalc.run()
