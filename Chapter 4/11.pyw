from graphics import *
def main():
    win=GraphWin("House",500,500)
    p1=win.getMouse()
    p2=win.getMouse()
    x1=p1.getX()
    x2=p2.getX()
    y1=p1.getY()
    y2=p2.getY()
    dx=x2-x1
    dy=y2-y1
    length=(dx**2+dy**2)**(1/2)
    frame=Rectangle(p1,p2)
    frame.draw(win)

    #Door
    door=win.getMouse()
    door_length=length/5
    door1=Point(door.getX()+(door_length/2),door.getY())
    door2=Point(door.getX()-(door_length/2),y1)
    Rectangle(door1,door2).draw(win)
    
    #Window
    center=win.getMouse()
    cx=center.getX()
    cy=center.getY()
    ww=door_length/4
    wp1=Point(cx-ww,cy-ww)
    wp2=Point(cx+ww,cy+ww)
    Rectangle(wp1,wp2).draw(win)

    #Roof
    roof=win.getMouse()
    Polygon(p2,roof,Point(x1,y2)).draw(win)
    input()
    win.close()
main()