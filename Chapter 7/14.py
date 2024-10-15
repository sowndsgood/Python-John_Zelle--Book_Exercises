# Chapter 4 Problem 7

from graphics import *
import math

def main():
    r:int=float(input("Enter the radius of circle:"))
    y:int=float(input("Enter the y-intercept of line:"))
    
    if r<y:
        print("Doesn't intersect")
    else:
        win=GraphWin("Circle Intersection",500,500)
        win.setCoords(-10,-10,10,10)
        circle=Circle(Point(0,0),r)
    
        line=Line(Point(-r,y),Point(r,y))
        x1=math.sqrt(r**2-y**2)
        x2=-x1
    
        Point1=Point(x1,y)
    
        Point1.setFill('red')
        Point2=Point(x2,y)
    
        Point2.setFill('red')

        circle.draw(win)
        line.draw(win)
        Point1.draw(win)
        Point2.draw(win)
        win.getKey()
        win.close()

        print("The values of x are:",x1,x2)
main()