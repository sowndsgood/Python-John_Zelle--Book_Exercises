#Modify event_loop3.py

from graphics import *

def handleKey(win,key)->None:

    if key=="r":
        win.setBackground("red")
    if key=="b":
        win.setBackground("blue")
    if key=="g":
        win.setBackground("green")
    if key=="y":
        win.setBackground("yellow")

def handlePt(win,pt)->None:

    box=Entry(pt,10)
    box.draw(win)

    while True:
        key=win.getKey()
        if key=="Escape": break

    box.undraw()
    text=box.getText()
    display=Text(pt,text)
    display.draw(win)


def main()->None:

    win=GraphWin("Window",500,500)
    
    while(True):

        key=win.checkKey()

        if key=="q":
            break
            
        if key:
            handleKey(win,key)

        pt=win.checkMouse()

        if pt:
            handlePt(win,pt)
        
    win.close()

main()


