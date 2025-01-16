#Random walk Simulation- 2D

from random import choice

#printing introduction
def printIntro()->None:
    print("This program is probabilistic simulation of random walk in 2D.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of steps:"))
    return n

def simWalk(n:int)->tuple[int,str,int,str]:
    x:int=0
    y:int=0
    steps:int=0
    for _ in range(n):
        res:str=choice(["Forward","Backward","Left","Right"])

        if res=="Forward": y+=1
        elif res=="Backward":y-=1
        elif res=="Right": x+=1
        elif res=="Left": x-=1

    if y<0: dir1='back' 
    else:dir1='front'
    if x<0: dir2='left' 
    else:dir2='right'

    return abs(y),dir1,abs(x),dir2

def main()->None:

    printIntro()

    n:int=getInputs()

    y,dir1,x,dir2=simWalk(n)

    print(f"You are {y} steps {dir1} and {x} steps {dir2} as far from starting point.")

main()