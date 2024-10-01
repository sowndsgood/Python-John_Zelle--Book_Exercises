#Draws several faces of varying size

from graphics import *

def drawFace(center, size, win)->None:

    #Face
    circle=Circle(center,size)
    circle.draw(win)

    x=center.getX()
    y=center.getY()

    #Right Eye
    right_eye=Circle(Point(x+size/2,y-size/2),size/5)
    right_eye.draw(win)

    #Left Eye
    left_eye=Circle(Point(x-size/2,y-size/2),size/5)
    left_eye.draw(win)

    #mouth
    mouth=Rectangle(Point(x-size/2,y+size/2),Point(x+size/2,y+size/2+size/5))
    mouth.draw(win)

win=GraphWin()
for i in range(5):
    center_x=int(input("Enter the center x-point:"))
    center_y=int(input("Enter the center y-point:"))
    center=Point(center_x,center_y)
    size=int(input("Enter the size:"))
    drawFace(center,size,win)

win.close()