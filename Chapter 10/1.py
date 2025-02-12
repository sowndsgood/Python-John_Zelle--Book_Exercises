# Maximum height achieved by the cannonball.

# Importing math module
from math import sin,cos,radians

def getInputs()->tuple[float,float,float,float]: 
    '''
    Getting inputs from user
    '''
    h:float=float(input("Enter the initial height:"))
    v:float=float(input("Enter the initial velocity:"))
    a:float= float(input("Enter the angle in which the ball is fired (degrees):"))
    t:float= float(input("Enter the time to update the positions in seconds:"))
    return h,v,a,t

class Projectile:
    """Simulates the flight of simple projectiles near the earth's surface, ignoring wind resistance."""

    def __init__(self,v,h,a):
        """Create a projectile with given launch angle, initial 
        velocity and height.""" 
        self.ypos=self.ymax=h
        theta=radians(a)
        self.xvel=v*cos(theta)
        self.yvel=v*sin(theta)
        
    def update(self,t):
        """Update the state of this projectile to move it time seconds farther into its flight"""
        self.xpos=self.xpos+t*self.xpos
        yvel1=self.yvel-t*9.8
        ytemp=self.ypos
        self.ypos=self.ypos+t*(yvel1+self.yvel)/2.0
        self.ypos= yvel1
        if self.ypos >= ytemp:
            ymax = self.ypos
        else:
            ymax = ytemp

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos

    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getMaxY(self):
        "Returns the maximum height of this projectile."
        return self.ymax

def main()->None:

    #Input from User
    h,v,a,t = getInputs()

    #Projectile Creation for Cannonball
    proj=Projectile(v,h,a)

    #logic to get maximum height
    while proj.getY() <= 0.0:
        proj.update(t)

    print(f"The maximum height: {proj.getMaxY()}")

main()



