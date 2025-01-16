#Pi Simulation

#importing random
from random import random

#printing introduction
def printIntro()->None:
    print("This program simulates throwing darts and approximation of Pi.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of darts to throw:"))
    return n

#Simulate Pi 
def simPi(n:int)->float:
    hit:int=0

    for i in range(n):
        x:float=2*random()-1
        y:float=2*random()-1

        if x**2 + y**2 <=1:
            hit+=1

    pi:float=4*hit/n
    return pi

def main()->None:
    
    printIntro()
    
    n:int=getInputs()

    pi:float = simPi(n)

    print(f"The approximate value of pi is: {pi:.4f}")

main()