from graphics import *

def main():
    win=GraphWin("Face",500,500)
    circle=Circle(Point(249,249),200)
    circle.draw(win)

    left_eye=Circle(Point(150,180),20)
    left_eye.draw(win)
    right_eye=Circle(Point(350,180),20)
    right_eye.draw(win)

    nose=Polygon(Point(249,249),Point(200,300),Point(300,300))
    nose.draw(win)

    mouth=Polygon(Point(170,350),Point(330,350),Point(170,375),Point(330,375))
    mouth.draw(win)
    win.getKey()
    win.close()

main()