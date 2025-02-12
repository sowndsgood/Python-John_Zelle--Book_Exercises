# Field of Vision using Monte Carlo simulation

#Importing Libraries
from random import uniform
import math

#printing introduction
def printIntro()->None:
    print("This program calculates the fraction of the field of vision occupied by the nearest wall.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of times to simulate:"))
    return n

def intersect(x1:float,y1:float,z1:float)->bool:
    if x1>0:
        a:float=3/6
        y1_intersect:float=a*y1
        z1_intersect:float=a*z1

        return abs(y1_intersect) <= 1 and abs(z1_intersect) <= 1

def simEach()->bool:
    x:float=0
    y:float=0
    z:float=0

    x=uniform(-1,1)
    y=uniform(-1,1)
    z=uniform(-1,1)

    l:float=math.sqrt(x**2+y**2+z**2)

    return intersect(x/l,y/l,z/l)

def simView(n:int)->int:
    hits:int=0
    for i in range(n):
        if simEach():
            hits+=1

    return hits

#Report
def report(hits:int,n:int)->None:
    print(f"The field of View is: {hits/n}")

#Main Function
def main()->None:
    printIntro()
    n:int=getInputs()
    hits=simView(n)
    report(hits,n)

main()

