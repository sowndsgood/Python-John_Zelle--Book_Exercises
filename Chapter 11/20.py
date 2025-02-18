# Cannonball Animation to adjust the initial height of the launcher

# Importing modules
import math
from graphics import *

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
    
class Launcher:

    def __init__(self, win):
        self.win = win
        self.circle = Circle(Point(0, 0.0), 3)
        self.circle.setFill('blue')
        self.circle.setOutline('blue')
        self.circle.draw(self.win)

        self.vel = 40.0
        self.angle = math.radians(45.0)
        self.height = 0.0

        self.arrow = Line(Point(0, 0), Point(0,0))
        self.redraw()

    def redraw(self):
        '''Changes velocity and angle of launcher'''

        self.arrow.undraw()
        self.circle.undraw()

        p2 = Point(self.vel*math.cos(self.angle), 
                   self.vel*math.sin(self.angle) + self.height)
        
        self.arrow = Line(Point(0, self.height), p2)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)
        self.arrow.draw(self.win)

        self.circle = Circle(Point(0, self.height), 3)
        self.circle.setFill('blue')
        self.circle.setOutline('blue')
        self.circle.draw(self.win)

    def adjAngle(self, amt):
        '''Adjust the angle of the launcher'''

        self.angle = self.angle + math.radians(amt)
        self.redraw()

    def adjVel(self, amt):
        '''Adjust the velocity of the launcher'''
        
        self.vel = self.vel + amt
        self.redraw()

    def adjHeight(self, amt):
        '''Adjusts the height of the launcher'''
        self.height = self.height + amt
        self.redraw()

    def fire(self):
        return shotTracker(self.win, math.degrees(self.angle), self.vel, self.height)

class ProjectileApp:
    def __init__(self):
        '''Initiates a window for the cannonball animation'''
        
        self.win = GraphWin("Cannonball animation", 640, 480)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(-10, 0), Point(210, 0)).draw(self.win)
        for x in range(0, 210, 50):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)

        self.launcher = Launcher(self.win)

        self.shots = []

    def run(self):
        '''Runs the entire cannonball animation'''

        while True:

            self.updateShots(1/30)

            key = self.win.checkKey()
            print(key)
            if key in ['Q', 'q']:
                #Breaks if q is clicked
                break
            elif key == 'Up':
                self.launcher.adjAngle(5)
            elif key == 'Down':
                self.launcher.adjAngle(-5)
            elif key == 'Left':
                self.launcher.adjVel(-5)
            elif key == 'Right':
                self.launcher.adjVel(5)
            elif key in ['f', 'F']:
                self.shots.append(self.launcher.fire())
            elif key == 'Prior':
                self.launcher.adjHeight(5)
            elif key == 'Next':
                self.launcher.adjHeight(-5)

            update(30)

        self.win.close()

    def updateShots(self, dt):
        '''Update the shots to newer position'''

        alive = []
        for shot in self.shots:
            shot.update(dt)

            if shot.getY() >= 0 or shot.getX() >= -10 or shot.getY() <= 210:
                alive.append(shot)
            else:
                shot.undraw()

        self.shots = alive

ProjectileApp().run()