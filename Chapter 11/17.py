# Class GraphicsGroup

from graphics import *

class GraphicsGroup:

    def __init__(self,anchor):
        '''Creates an empty group with the given anchor point'''
        self.anchor=anchor
        self.group=[]

    def getAnchor(self):
        '''Returns a clone of the anchor point'''
        return self.anchor.clone()

    def addObject(self,gObject):
        '''Adds gObject to the group'''
        self.group.append(gObject)

    def move(self,dx,dy):
        '''Moves all of the objects in the group'''
        self.anchor.move(dx,dy)
        for i in self.group:
            i.move(dx,dy)

    def draw(self,win):
        '''Draws all the objects in the group into win'''
        for i in self.group:
            i.draw(win)

    def undraw(self):
        '''Undraws all the objects in the group'''
        for i in self.group:
            i.undraw()

def main():

    win=GraphWin("Car",600,400)
    win.setBackground("lightblue")

    anchor=Point(300,200)

    car=GraphicsGroup(anchor)

    body = Rectangle(Point(250, 220), Point(400, 270))
    body.setFill("red")

    roof = Polygon(Point(280, 220), Point(370, 220), Point(350, 190), Point(300, 190))
    roof.setFill("black")

    left_wheel = Circle(Point(270, 275), 15)
    left_wheel.setFill("black")

    right_wheel = Circle(Point(380, 275), 15)
    right_wheel.setFill("black")

    front_window = Rectangle(Point(305, 195), Point(340, 220))
    front_window.setFill("lightgrey")

    car.addObject(body)
    car.addObject(roof)
    car.addObject(left_wheel)
    car.addObject(right_wheel)
    car.addObject(front_window)

    car.draw(win)

    while True:
        click = win.getMouse()  
        dx = click.getX() - car.getAnchor().getX()
        dy = click.getY() - car.getAnchor().getY()
        car.move(dx, dy)  

    win.close()

main()