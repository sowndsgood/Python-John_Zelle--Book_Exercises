# Cannonball animation to include target objects

# Importing modules
import math
from graphics import *
import random

#Projectile Class
class Projectile:
    """This class will take care of object that is in Projectileion"""

    def __init__(self, angle, velocity, height):
        """It initialises x and y pos of the Projectile ball"""
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
        self.marker.setFill('blue')
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
    
    def getCenter(self):
        '''Returns the center of the Cannonball'''
        return self.marker.getCenter()
    
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
        self.circle.setFill('red')
        self.circle.setOutline('red')
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
    
class Target:

    def __init__(self, win):
        '''Creates the target with a random size'''
        self.win = win
        self.createTarget()

    def createTarget(self):
        '''Generates a new random target'''
        x = random.randint(30, 200) 
        width = random.randint(10, 30) 
        height = random.randint(10, 40)  

        self.p1 = Point(x - width, height)
        self.p2 = Point(x, 0)
        self.tar = Rectangle(self.p1, self.p2)
        self.tar.setFill("green")  
        self.tar.draw(self.win)

    def changeTarget(self):
        '''Changes the target's position and size'''
        self.tar.undraw() 
        self.createTarget() 

    def target_clicked(self, pt):
        '''Checks whether the target is hit by the cannonball'''
        print(self.tar.getP1(), self.tar.getP2())
        return (self.tar.getP1().getX() <= pt.getX() <= self.tar.getP2().getX()) and \
                (self.tar.getP2().getY() <= pt.getY() <= self.tar.getP1().getY())

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

        self.tar = Target(self.win)
        self.targetHits = 0
        self.text = Text(Point(100, 90), f"You have hit the target: {self.targetHits} times ")
        self.text.draw(self.win)

    def run(self):
        '''Runs the entire cannonball animation'''

        while True:
            
            self.updateShots(1/20)
            self.text.setText(f"You have hit the target: {self.targetHits} times ")

            key = self.win.checkKey()
            print(key)
            if key in ['Q', 'q']:
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
            pt = shot.getCenter()

            print(pt)
            if self.tar.target_clicked(pt):
                shot.undraw()
                self.tar.changeTarget()
                self.targetHits += 1
            if (-10 <= shot.getX() <= 210) and (0<= shot.getY() <= 155):
                alive.append(shot)
            else:
                shot.undraw()

        self.shots = alive

ProjectileApp().run()