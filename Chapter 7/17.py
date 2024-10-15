# Circle Bouncing around Window

from graphics import *

def main()->None:

    dx=1
    dy=1

    win=GraphWin("Circle Bouncing",800,800)
    Rectangle(Point(10,10),Point(790,790)).draw(win)
    circle=Circle(Point(50,300),50).draw(win)

    for i in range(10000):
        point=circle.getCenter()
        x=point.getX()
        y=point.getY()
        if x<0 or x>750:
            dx-=1
        if y<0 or y>750:
            dy-=1
        
        circle.move(dx,dy)
        update(30)
        
    win.close()
main()