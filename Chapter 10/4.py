# Simulate Three Button Monte

from graphics import *
from random import choice

class Door:

    def __init__(self,x1,y1,x2,y2,win,type):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        button=Rectangle(Point(x1,y1),Point(x2,y2))
        if type=='door':
            button.setFill('blue')
            button.draw(win)
        else:
            button.setFill('red')
            button.draw(win)
            Text(Point(610,410),"QUIT").draw(win)
        
    def click(self,p):
        return self.x1<=p.getX()<=self.x2 and self.y1<=p.getY()<=self.y2

def main()->None:
    win=GraphWin("Three Button Monte",1000,500)

    text=Text(Point(500,50),"Choose a box")
    text.draw(win)
    
    Door_1=Door(100,100,300,300,win,'door')
    Door_2=Door(400,100,600,300,win,'door')
    Door_3=Door(700,100,900,300,win,'door')
    Quit=Door(590,390,630,430,win,'quit')

    wins:int=0
    loss:int=0

    result= Text(Point(500, 450), "")
    score= Text(Point(500, 470), "")

    while True:


        p=win.getMouse()

        result.undraw()
        score.undraw()

        if Quit.click(p):
            break
        if Door_1.click(p):
            clicked="Door1"
        elif Door_2.click(p):
            clicked="Door2"
        elif Door_3.click(p):
            clicked="Door3"

        correct=choice(["Door1","Door2","Door3"])
        if correct==clicked:
            result=Text(Point(500,450),"Won")
            wins+=1
        else:
            result=Text(Point(500,450),f"Loss. Correct Door : {correct}")
            loss+=1

        score=Text(Point(500,470),f"Win:{wins} Loss:{loss} Total Matches:{wins+loss}")

        result.draw(win)
        score.draw(win)
    
    win.getMouse()
    win.close()

main()
