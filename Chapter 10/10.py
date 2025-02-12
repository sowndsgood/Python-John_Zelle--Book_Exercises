#New class for Cube

import math

class Cube:

    def __init__(self, length):
        '''Creates a cube having the given radius.'''
        self.length=length

    def getRadius(self)->float:
        '''Returns the length of cube.'''
        return self.length

    def surfaceArea(self)->float:
        '''Returns the surface area of the cube. '''
        return 6*(self.length**2)

    def volume(self)->float:
        '''Returns the volume of the cube.'''
        return self.length**3

def main()->None:
    length=float(input("Enter the length:"))
    cube1=Cube(length)
    
    print("The Volume is",cube1.volume(),"cubic units")
    print("The Surface area is",cube1.surfaceArea(),"square units")
    
main()

