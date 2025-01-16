#Random walk Simulation

from random import choice

#printing introduction
def printIntro()->None:
    print("This program is probabilistic simulation of random walk.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of steps:"))
    return n

def simWalk(n:int)->float:
    steps:int=0
    for _ in range(n):
        res:str=choice(["Head","Tail"])

        if res=="Head":
            steps+=1
        else:
            steps-=1

    return abs(steps)

def main()->None:

    printIntro()

    n:int=getInputs()

    avg:float=simWalk(n)

    print(f"The average steps is:{avg}")

main()