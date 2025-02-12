#New class to solve Programming Exercise 1 from Chapter 3.

import math

class Sphere:

    def __init__(self, radius):
        '''Creates a sphere having the given radius.'''
        self.radius=radius

    def getRadius(self)->float:
        '''Returns the radius of this sphere.'''
        return self.radius

    def surfaceArea(self)->float:
        '''Returns the surface area of the sphere. '''
        return 4*math.pi*(self.radius**2)

    def volume(self)->float:
        '''Returns the volume of the sphere.'''
        return (4*math.pi*(self.radius**3))/3

def main()->None:
    radius=float(input("Enter the radius:"))
    sphere1=Sphere(radius)
    
    print("The Volume is",sphere1.volume(),"cubic units")
    print("The Surface area is",sphere1.surfaceArea(),"square units")
    
main()

