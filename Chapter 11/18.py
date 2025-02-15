# Extend the random walk program from Chapter 9 (Programming Exercise 12)

#Random walk Simulation

from random import choice

#printing introduction
def printIntro()->None:
    print("This program is probabilistic simulation of random walk.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the length of side walk:"))
    return n

def simWalk(n:int)->float:

    current=n//2
    dict={}
    for i in range(1,n+1):
        dict[i]=0
        
    while 0<current<n:
    
        res:str=choice(["Head","Tail"])

        if res=="Head":
            current+=1
        else:
            current-=1

        if 0<current<n:
            dict[current]=dict.get(current,0)+1

    return dict


def main()->None:

    printIntro()

    n:int=getInputs()

    dict=simWalk(n)

    for key,value in dict.items():
        print(f"Square {key}: {value}")

main()