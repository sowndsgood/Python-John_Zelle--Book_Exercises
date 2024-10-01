# Circle is moved where the user clicked.

from graphics import *

def moveTo(shape,newCenter)->None:
    oldCenter=shape.getCenter()
    dx=newCenter.getX()-oldCenter.getX()
    dy=newCenter.getY()-oldCenter.getY()
    text=Text(newCenter,str(newCenter))
    text.draw(win)
    shape.move(dx,dy)

win=GraphWin("Moving Circle",1000,1000)

shape=Circle(Point(500,500),50)
shape.setFill('red')
shape.setOutline('green')
shape.setWidth(5)
shape.draw(win)

for i in range(10):

    newCenter=win.getMouse()
    moveTo(shape,newCenter)
    
win.close()