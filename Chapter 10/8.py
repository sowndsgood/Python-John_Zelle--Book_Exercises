# DieView Class with new method for color 

from graphics import *
from random import randrange

class Button:
    '''A button is a labeled rectangle in a window. It is activated or deactivated with the activate() and deactivate() methods. The clicked(p) method returns true if the button is active and p is inside it.'''

    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button."""

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax = x-w, w+x
        self.ymin, self.ymax = y-h, h+y
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)
        self.rect.setFill('white')
        self.rect.setWidth(1)
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
        

    def clicked(self, pt):
        """Return True if button is 'active' and pt is inside the button."""
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def getLabel(self):
        """Returns the text in the label."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False


#dice class creation
class DieView:
    """ DieView is a widget that displays a graphical representation 
        of a standard six-sided die."""
    def __init__(self, win, center, size):
        """Creates a view of die
        """

        #first define some standard values 
        self.win = win
        self.background = 'white'
        self.foreground = 'black'

        self.psize = 0.1 * size
        hsize = size/2.0
        offset = 0.6 * hsize

        #create a square for the face
        cx, cy = center.getX(), center.getY()
        pt1 = Point(cx-hsize, cy-hsize)
        pt2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(pt1, pt2)
        rect.setFill(self.background)
        rect.draw(win)

        #Create 7 circles for standard pip locations 
        self.pip1 = self.__makepip(cx-offset, cy+offset)
        self.pip2 = self.__makepip(cx-offset, cy)
        self.pip3 = self.__makepip(cx-offset, cy-offset)
        self.pip4 = self.__makepip(cx, cy)
        self.pip5 = self.__makepip(cx+offset, cy+offset)
        self.pip6 = self.__makepip(cx+offset, cy)
        self.pip7 = self.__makepip(cx+offset, cy-offset)

        #Draw an initial value 
        self.value = 1
        self.setValue(self.value)

    def __makepip(self, x, y):
        "Internal helper method to draw a pip at (x,y)" 
        pip = Circle(Point(x,y), self.psize) 
        pip.setFill(self.background) 
        pip.setOutline(self.background) 
        pip.draw(self.win) 
        return pip 

    def setColor(self, color):
        '''Set dice to specific color'''
        self.foreground = color
        self.setValue(self.value)

    def setValue(self, value):
            "Set this die to display value."

            self.value = value
            #initial white background for the pips to disappear
            self.pip1.setFill(self.background)
            self.pip2.setFill(self.background)
            self.pip3.setFill(self.background)
            self.pip4.setFill(self.background)
            self.pip5.setFill(self.background)
            self.pip6.setFill(self.background)
            self.pip7.setFill(self.background)

            # turn correct pips on
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
    win = GraphWin("Dice roller", 1000, 700)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    #draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = Button(win, Point(5, 4.5), 2, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5, 1), 2, 1, "Quit")

    #Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):

            #RGB range
            color = color_rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))

            #Die1 
            value1 = randrange(1, 7)
            die1.setValue(value1)
            die1.setColor(color)

            #Die2 
            value2 = randrange(1, 7)
            die2.setValue(value2)
            die2.setColor(color)

            quitButton.activate()

        pt = win.getMouse()

    win.close()

main()
        