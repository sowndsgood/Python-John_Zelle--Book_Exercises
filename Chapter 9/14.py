#Random walk Simulation in any direction

from random import random
from graphics import *
import math

#printing introduction
def printIntro()->None:
    print("This program is probabilistic simulation of random walk and graphical visualisation.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of steps:"))
    return n

def simWalk(n:int)->tuple[int,str,int,str]:

    win=GraphWin("Random Walk",1000,1000)
    x:float=500
    y:float=500
    for i in range(n):
        angle=random()*2*math.pi
        new_x=x+math.cos(angle)
        new_y=y+math.sin(angle)

        Line(Point(x,y),Point(new_x,new_y)).draw(win)

        x=new_x
        y=new_y

    win.getKey()
    win.close()

def main()->None:

    printIntro()

    n:int=getInputs()

    simWalk(n)

main()