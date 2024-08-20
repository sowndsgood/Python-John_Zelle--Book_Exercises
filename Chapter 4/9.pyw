from graphics import *

def main():
    win=GraphWin("Rectangle",500,500)
    p1=win.getMouse()
    p2=win.getMouse()
    x1:int=p1.getX()
    y1:int=p1.getY()
    x2:int=p2.getX()
    y2:int=p2.getY()
    p3=Point(x2,y1)
    p4=Point(x1,y2)
    line1=Line(p1,p3)
    line2=Line(p2,p3)
    line3=Line(p4,p2)
    line4=Line(p1,p4)
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    length:int=x2-x1
    width:int=y2-y1
    print("The area is:",length*width)
    print("The perimeter is:",2*(length+width))
    input()
    win.close()
main()