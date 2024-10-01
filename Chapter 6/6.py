#Programming Exercise 9 from Chapter 3

import math 
from graphics import * 

def triangle_area(a,b,c)->float:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def square(x)->float: 
    return x ** 2 

def distance(p1, p2)->float: 
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY())) 
    return dist

def draw()->None:
    win = GraphWin("Draw a Triangle") 
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points") 
    message.draw(win) 
    # Get and draw three vertices of triangle 
    p1 = win.getMouse() 
    p1.draw(win) 
    p2 = win.getMouse() 
    p2.draw(win) 
    p3 = win.getMouse() 
    p3. draw(win) 
    # Use Polygon object to draw the triangle 
    triangle = Polygon(p1,p2,p3) 
    triangle.setFill("peachpuff") 
    triangle.setOutline("cyan") 
    triangle.draw(win) 

    # Calculate the perimeter of the triangle 
    a=distance(p1,p2) 
    b=distance(p2,p3) 
    c=distance(p3,p1) 

    area=triangle_area(a,b,c)

    message.setText("The area is: {0:0.2f}".format(area)) 
    # Wait for another click to exit 
    win.getMouse() 
    win. close()

draw()