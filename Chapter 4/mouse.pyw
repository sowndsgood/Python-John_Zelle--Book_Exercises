from graphics import *
def main():
    win=GraphWin("Click any point")
    p=win.getMouse()
    print("The point is:",p.getX(),p.getY())
main()
