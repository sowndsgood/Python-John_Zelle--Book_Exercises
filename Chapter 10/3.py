# Simulate Three Button Monte

from graphics import *
from random import choice

class Door:

    def __init__(self,x1,y1,x2,y2,win):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        button=Rectangle(Point(x1,y1),Point(x2,y2))
        button.setFill('blue')
        button.draw(win)

    def click(self,p):
        if self.x1<=p.getX()<=self.x2 and self.y1<=p.getY()<=self.y2:
            return True


def main()->None:
    win=GraphWin("Three Button Monte",1000,500)

    text=Text(Point(500,50),"Choose a box")
    text.draw(win)
    
    Door_1=Door(100,100,300,300,win)
    Door_2=Door(400,100,600,300,win)
    Door_3=Door(700,100,900,300,win)

    p=win.getMouse()

    if Door_1.click(p):
        clicked="Door1"
    elif Door_2.click(p):
        clicked="Door2"
    elif Door_3.click(p):
        clicked="Door3"

    correct=choice(["Door1","Door2","Door3"])
    if correct==clicked:
        Text(Point(500,450),"Won").draw(win)
    else:
        Text(Point(500,450),f"Loss. Correct Door : {correct}").draw(win)
    
    win.getMouse()
    win.close()

main()
