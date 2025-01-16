#simulation to estimate the probability of rolling five of a kind in a single roll of five six-sided dice.

from random import randint

#printing introduction
def printIntro()->None:
    print("This program simulates to estimate the probability of rolling five of a kind in a single roll of five six-sided dice.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of rolls:"))
    return n

def simDices(n:int)->None:
    total:int=0
    for i in range(n):
        d1:int=randint(1,6)
        d2:int=randint(1,6)
        d3:int=randint(1,6)
        d4:int=randint(1,6)
        d5:int=randint(1,6)

        if d1==d2==d3==d4==d5:
            total+=1

    print(f"The probability is:{total/n:.4f}")

def main()->None:
    printIntro()

    n:int=getInputs()

    simDices(n)

main()