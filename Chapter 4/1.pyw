from graphics import *
def main():
    win=GraphWin("Graphical Window",9500,600)
    shape=Rectangle(Point(100,100),Point(160,160))
    shape.setOutline('yellow')
    shape.setFill('cyan')
    shape.draw(win)
    x1=shape.getP1()
    y1=shape.getP2()
    for i in range(5):
        p=win.getMouse()
        c=shape.getCenter()
        X=p.getX()
        Y=p.getY()
        square=Rectangle(Point(X-30,Y-30),Point(X+30,Y+30))
        square.setOutline('yellow')
        square.setFill('cyan')
        shape.undraw()
        square.draw(win)
    text=Text(Point(400,50),"Click again to exit.")
    text.draw(win)
    key=win.getKey()
    win.close()
main()

    

