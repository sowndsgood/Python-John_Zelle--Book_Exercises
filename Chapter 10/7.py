# CButton Class for roller.py 

from cbutton import CButton

from graphics import *
from random import randrange

#dice class creation
class DieView:
    """ DieView is a widget that displays a graphical representation of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Creates a view of a die."""

        #first define some standard values 
        self.win = win
        self.background = 'white'
        self.foreground = 'black'

        self.psize = 0.1 * size
        hsize = size/2.0
        offset = 0.6 * hsize

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        pt1 = Point(cx-hsize, cy-hsize)
        pt2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(pt1, pt2)
        rect.setFill(self.background)
        rect.draw(win)

        # Create 7 circles for standard pip locations 
        self.pip1 = self.__makepip(cx-offset, cy+offset)
        self.pip2 = self.__makepip(cx-offset, cy)
        self.pip3 = self.__makepip(cx-offset, cy-offset)
        self.pip4 = self.__makepip(cx, cy)
        self.pip5 = self.__makepip(cx+offset, cy+offset)
        self.pip6 = self.__makepip(cx+offset, cy)
        self.pip7 = self.__makepip(cx+offset, cy-offset)

        #Draw an initial value 
        self.setValue(1)

    def __makepip(self, x, y):
        "Internal helper method to draw a pip at (x,y)" 
        pip = Circle(Point(x,y), self.psize) 
        pip.setFill(self.background) 
        pip.setOutline(self.background) 
        pip.draw(self.win) 
        return pip 

    def setValue(self, value):
            "Set this die to display value."

            # turn all pips off
            self.pip1.setFill(self.background)
            self.pip2.setFill(self.background)
            self.pip3.setFill(self.background)
            self.pip4.setFill(self.background)
            self.pip5.setFill(self.background)
            self.pip6.setFill(self.background)
            self.pip7.setFill(self.background)

            # turn correct pip on
            if value == 1:
                self.pip4.setFill(self.foreground)
            elif value == 2:
                self.pip5.setFill(self.foreground)
                self.pip3.setFill(self.foreground)
            elif value == 3:
                self.pip5.setFill(self.foreground)
                self.pip4.setFill(self.foreground)
                self.pip3.setFill(self.foreground)
            elif value == 4:
                self.pip1.setFill(self.foreground)
                self.pip5.setFill(self.foreground)
                self.pip3.setFill(self.foreground)
                self.pip7.setFill(self.foreground)
            elif value == 5:
                self.pip1.setFill(self.foreground)
                self.pip5.setFill(self.foreground)
                self.pip3.setFill(self.foreground)
                self.pip7.setFill(self.foreground)
                self.pip4.setFill(self.foreground)
            else:
                self.pip1.setFill(self.foreground)
                self.pip5.setFill(self.foreground)
                self.pip3.setFill(self.foreground)
                self.pip7.setFill(self.foreground)
                self.pip2.setFill(self.foreground)
                self.pip6.setFill(self.foreground)


#main function
def main():

    #create the application window 
    win = GraphWin("Dice roller",1000,700)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    #Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = CButton(win, Point(5, 4.5), 1, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(5, 2), 1, "Quit")

    #Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    win.close()

main()
            
