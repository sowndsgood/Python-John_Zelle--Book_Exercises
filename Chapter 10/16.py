###Program: Cannonball simulation

from graphics import *
import math
import random

class Projectile:
    """This class will take care of object that is in projection"""

    def __init__(self, angle, velocity, height):
        """It initialises x and y pos of the projectile ball"""
        theta = math.radians(angle)
        self.xpos = 0.0
        self.ypos = height
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def update(self, dt):
        """Updates the position of the ball for the given time interval"""
        self.xpos = self.xpos + self.xvel * dt
        self.yvel = self.yvel - dt * 9.8
        self.ypos = self.ypos + dt * self.yvel

    def getX(self):
        """Returns the X position of object."""
        return self.xpos
    
    def getY(self):
        """Returns the Y position of object."""
        return self.ypos



class shotTracker:
    """Creates a object for circle representing the cannonball with its properties.
    """
    def __init__(self, win, angle, velocity, height):
        """Creates cannon ball both in GUI and with its properties"""
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, 0), 3)
        self.marker.setFill('red')
        self.marker.setOutline('black')
        self.marker.draw(win)

    def update(self, dt):
        """Updates the cannon ball position with respect to time dt"""
        self.proj.update(dt)

        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()

        #moving the cannonball
        self.marker.move(dx, dy)
    
    def getX(self):
        """Returns the X position of cannonball"""
        return self.proj.getX()
    
    def getY(self):
        """Returns the Y position of cannonball"""
        return self.proj.getY()
    
    def undraw(self):
        """Undraws the cannonball"""
        self.marker.undraw()



class Button:
    '''A button is a labeled triangle in a window.
    It is activated or deactivated by using the functions activate() and deactivate() respectively.
    The clicked(pt) method will check if the button was clicked by checking the button was active and the
    pt is inside the rectangle and return 'True'.
    '''

    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button."""

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax = x-w, w+x
        self.ymin, self.ymax = y-h, h+y
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)
        self.rect.setFill('lightgrey')
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



class inputDialog:
    """This class is for input Dialog box where we can give initial angle, velocity and height of cannonball """

    def __init__(self, angle, velocity, height):
        '''It creates the input dialog box'''
        self.win = win = GraphWin("Dialog box", 200, 300)
        win.setCoords(0, 0, 10, 10)

        #angle input box
        Text(Point(3, 8), "Angle").draw(win)
        self.angle = Entry(Point(7.5, 8), 5).draw(win)
        self.angle.setText(str(angle))

        #velocity input box
        Text(Point(3, 6), "Velocity").draw(win)
        self.velocity = Entry(Point(7.5, 6), 5).draw(win)
        self.velocity.setText(str(velocity))

        #height input box
        Text(Point(3, 4), "Height").draw(win)
        self.height = Entry(Point(7.5, 4), 5).draw(win)
        self.height.setText(str(height))

        #creating buttons 
        self.fire = Button(win, Point(2.5, 2), 2.5, 1, "Fire!")
        self.fire.activate()

        self.quit = Button(win, Point(7.5, 2), 2.5, 1, "Quit")
        self.quit.activate()

    def interact(self):
        """To get the key pressed"""
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "quit"

            if self.fire.clicked(pt):
                return "fire!"
            
    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.velocity.getText())
        h = float(self.velocity.getText())

        return a, v, h
            
    def close(self):
        """Closes the input dialog window"""
        self.win.close()

class Target:
    """Creates a target to hit"""
    
    def __init__(self, win):
        """Creates a random rectangle along x-axis"""
        x = random.randint(0, 210)

        self.p1 = Point(x-5, 10)
        self.p2 = Point(x+5, 0)
        rect = Rectangle(self.p1, self.p2)
        rect.draw(win)
        rect.setWidth(2)


    def target_hit(self, shot):
        """Checks whther the shot is hit on the target"""
        return self.p1.getX() <= shot.getX() <= self.p2.getX()
                 

def main()->None:

    win = GraphWin("Cannonball simulation", 1000, 600, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    #drawing line and scale points
    Line(Point(-10, 0), Point(210, 0)).draw(win)

    for i in range(0, 210, 25):
        Line(Point(i, 0), Point(i, 2)).draw(win)
        Text(Point(i, -4), str(i)).draw(win)

    angle, velocity, height = 45, 30, 2.0

    #creating the input dialog box
    dialog = inputDialog(angle, velocity, height)

    #creating the target
    target = Target(win)

    while True:
        clicked_option = dialog.interact()

        if clicked_option == "quit":
            break
        
        angle, velocity, height = dialog.getValues()
        shot = shotTracker(win, angle, velocity, height)
        
        while -10 <= shot.getX() <= 210 and 0<= shot.getY():
            shot.update(1/50)
            update(50)

        if target.target_hit(shot):
            break

    Text(Point(100,10),"You have hit the target. Hurray!!!").draw(win)
    time.sleep(5)
    win.close()

main()
    