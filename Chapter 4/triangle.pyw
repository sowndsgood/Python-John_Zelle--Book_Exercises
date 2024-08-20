from graphics import *
def main():
    win=GraphWin()
    win.setCoords(0,0,10,10)
    message=Text(Point(5,0.5),"Draw a triangle")
    message.draw(win)

    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)

    triangle=Polygon(p1,p2,p3)
    triangle.setFill("cyan")
    triangle.setOutline("red")
    triangle.setWidth("2")
    triangle.draw(win)

    message.setText("Click any point to exit")
    win.getMouse()
main()