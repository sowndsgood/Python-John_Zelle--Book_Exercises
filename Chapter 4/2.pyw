from graphics import *
def main():
    win=GraphWin("Archery Target",300,300)
    radius=25
    circlew=Circle(Point(150,150),50)
    circlew.setFill('white')
    circlew.draw(win)
    circleb=Circle(Point(150,150),40)
    circleb.setFill('black')
    circleb.draw(win)
    circlebl=Circle(Point(150,150),30)
    circlebl.setFill('blue')
    circlebl.draw(win)
    circler=Circle(Point(150,150),20)
    circler.setFill('red')
    circler.draw(win)
    circley=Circle(Point(150,150),10)
    circley.setFill('yellow')
    circley.draw(win)
    p=win.getMouse()
    win.close()
main()