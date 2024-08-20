from graphics import *

def main():
    win=GraphWin("Dice",1200,300)

    Dice1=Polygon(Point(40,50),Point(240,50),Point(240,250),Point(40,250))
    Dice1.draw(win)

    Dice2=Polygon(Point(270,50),Point(470,50),Point(470,250),Point(270,250))
    Dice2.draw(win)

    Dice3=Polygon(Point(500,50),Point(700,50),Point(700,250),Point(500,250))
    Dice3.draw(win)

    Dice4=Polygon(Point(730,50),Point(930,50),Point(930,250),Point(730,250))
    Dice4.draw(win)

    Dice5=Polygon(Point(960,50),Point(1160,50),Point(1160,250),Point(960,250))
    Dice5.draw(win)

    d1=Circle(Point(140,150),10)
    d1.setFill('black')
    d1.draw(win)

    d2left=Circle(Point(320,90),10)
    d2left.setFill('black')
    d2left.draw(win)

    d2right=Circle(Point(430,210),10)
    d2right.setFill('black')
    d2right.draw(win)

    d3left=Circle(Point(540,90),10)
    d3left.setFill('black')
    d3left.draw(win)

    d3right=Circle(Point(670,210),10)
    d3right.setFill('black')
    d3right.draw(win)

    d3=Circle(Point(600,150),10)
    d3.setFill('black')
    d3.draw(win)

    d4lefttop=Circle(Point(770,90),10)
    d4lefttop.setFill('black')
    d4lefttop.draw(win)

    d4rightdown=Circle(Point(890,210),10)
    d4rightdown.setFill('black')
    d4rightdown.draw(win)

    d4righttop=Circle(Point(890,90),10)
    d4righttop.setFill('black')
    d4righttop.draw(win)

    d4leftdown=Circle(Point(770,210),10)
    d4leftdown.setFill('black')
    d4leftdown.draw(win)

    d5lefttop=Circle(Point(1000,90),10)
    d5lefttop.setFill('black')
    d5lefttop.draw(win)

    d5rightdown=Circle(Point(1120,210),10)
    d5rightdown.setFill('black')
    d5rightdown.draw(win)

    d5righttop=Circle(Point(1120,90),10)
    d5righttop.setFill('black')
    d5righttop.draw(win)

    d5leftdown=Circle(Point(1000,210),10)
    d5leftdown.setFill('black')
    d5leftdown.draw(win)

    d3=Circle(Point(1060,150),10)
    d3.setFill('black')
    d3.draw(win)

    win.getKey()
    win.close()

main()