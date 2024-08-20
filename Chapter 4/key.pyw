from graphics import *
def main():
    win=GraphWin()
    p=win.getMouse()
    p.draw(win)
    k=win.getKey()
    label=Text(p,k)
    label.draw(win)
main()