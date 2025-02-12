from graphics import *
from random import randrange

class CButton:
    '''A button is a labeled rectangle in a window. It is activated or deactivated with the activate() and deactivate() methods. The clicked(p) method returns true if the button is active and p is inside it.'''

    def __init__(self, win, center, radius, label):
        """Creates a circular button."""

        self.radius = radius
        self.center = center
        self.circle = Circle(center, radius)
        self.circle.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
        
    def clicked(self, pt):
        """Return True if button is 'active' and pt is inside the button."""
        return (self.active and
                self.radius >= ((pt.getX() - self.center.getX())**2 + (pt.getY() - self.center.getY()) **2 ) ** 0.5 )

    def getLabel(self):
        """Returns the text in the label."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
