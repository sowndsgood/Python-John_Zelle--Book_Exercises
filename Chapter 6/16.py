# Photo Anonymizer

from graphics import *
import math

def drawFace(center, size, win)->None:

    #Face
    circle=Circle(center,size)
    circle.setFill('blue')
    circle.draw(win)

    x=center.getX()
    y=center.getY()

    #Right Eye
    right_eye=Circle(Point(x+size/2,y-size/2),size/5)
    right_eye.setFill('black')
    right_eye.draw(win)

    #Left Eye
    left_eye=Circle(Point(x-size/2,y-size/2),size/5)
    left_eye.setFill('black')
    left_eye.draw(win)

    #mouth
    mouth=Rectangle(Point(x-size/2,y+size/2),Point(x+size/2,y+size/2+size/5))
    mouth.draw(win)

win=GraphWin("Image Anonymizer",500,500)
filename=input("Enter the filename:")
image=Image(Point(250,250),filename)
image.draw(win)
n=int(input("Enter the number of faces:"))
for i in range(n):
    
    center=win.getMouse()
    
    edge=win.getMouse()
    x1=center.getX()
    y1=center.getY()
    x2=edge.getX()
    y2=edge.getY()
    size=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    drawFace(center,size,win)
win.close()




