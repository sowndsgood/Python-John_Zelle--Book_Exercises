# Chapter 4 Problem 8

from graphics import *
import math

def main()->None:
    win=GraphWin("Line",500,500)
    p1=win.getMouse()
    p2=win.getMouse()
    line=Line(p1,p2)
    line.draw(win)
    xm=(p1.getX()+p2.getX())/2
    ym=(p1.getY()+p2.getY())/2
    mid=Point(xm,ym)
    mid.setFill('cyan')
    mid.draw(win)
    x1:int=p1.getX()
    x2:int=p2.getX()
    y1:int=p1.getY()
    y2:int=p2.getY()
    dx:int=x1-x2
    dy:int=y1-y2
    if dx==0:
        print("The line is vertical.")
    else:
        len=math.sqrt(dx**2+dy**2)
        print("The slope is :",dy/dx)
        print("The length is :",len)
        win.getKey()
        win.close()
main()