from graphics import *

def main():
    win=GraphWin("Christmas",500,500)
    t1=Polygon(Point(50,20),Point(10,100),Point(90,100))
    t1.draw(win)
    t2=Polygon(Point(30,100),Point(70,100),Point(90,150),Point(10,150))
    t2.draw(win)
    t3=Polygon(Point(30,150),Point(70,150),Point(90,200),Point(10,200))
    t3.draw(win)
    b=Polygon(Point(40,200),Point(60,200),Point(60,250),Point(40,250))
    b.draw(win)
    

    c3=Circle(Point(225,340),80)
    c3.draw(win)
    c2=Circle(Point(225,200),60)
    c2.draw(win)
    c1=Circle(Point(225,100),40) #Face Center
    c1.draw(win)
    eye1=Circle(Point(215,95),5)
    eye1.draw(win)
    eye2=Circle(Point(235,95),5)
    eye2.draw(win)
    nose=Polygon(Point(225,105),Point(225,110),Point(240,107))
    nose.draw(win)

    t1l=Polygon(Point(400,20),Point(360,100),Point(440,100))
    t1l.draw(win)
    t2l=Polygon(Point(380,100),Point(420,100),Point(440,150),Point(360,150))
    t2l.draw(win)
    t3l=Polygon(Point(380,150),Point(420,150),Point(440,200),Point(360,200))
    t3l.draw(win)
    bl=Polygon(Point(390,200),Point(410,200),Point(410,250),Point(390,250))
    bl.draw(win)

    win.getKey()
main()