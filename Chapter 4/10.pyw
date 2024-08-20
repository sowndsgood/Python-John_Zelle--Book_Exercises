from graphics import *

def main():
    win = GraphWin('Triangle Information', 500, 500)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle=Polygon(p1, p2, p3)
    triangle.draw(win)

    dx1 = abs(p1.getX() - p2.getX())
    dy1 = abs(p1.getX() - p2.getY())
    a = ((dx1**2) + (dy1**2))**(1/2)

    dx2 = abs(p2.getX() - p3.getX())
    dy2 = abs(p2.getX() - p3.getY())
    b = ((dx2**2) + (dy2**2))**(1/2)

    dx3 = abs(p1.getX() - p3.getX())
    dy3 = abs(p1.getX() - p3.getY())
    c = ((dx3**2) + (dy3**2))**(1/2)

    s=(a+b+c)/2
    area=s*(s+1)*(s+2)
    print("The perimeter is:",a+b+c)
    print("The area is:",area)
    win.getKey()
    win.close()

main()