#Blackjack Game

#importing random
from random import randint

#printing introduction
def printIntro()->None:
    print("This program simulates multiple games of blackjack and estimates the probability that the dealer will bust.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of games:"))
    return n 

def simOneGame()->bool:
    hasAce:bool=False
    total:int=0
    while True:
        card=randint(1,13)
        if card>=10: score=10
        elif card==1:
            score=1 
            hasAce=True
        else: score=card

        total+=score
        if hasAce and total+10<=21:
            new=total+10
        else:
            new=total

        if 17<=new<=21:
            return False
        elif new>21:
            return True

def simNGames(n:int)->int:
    return sum(simOneGame() for _ in range(n))

#Report
def report(total:int,n:int)->None:
    print(f"Total games won:{total}")
    print(f"Probability of winning: {total/n:.4f}")
    print(f"Percentage of winning: {total*100/n:.4f} %")

def main()->None:
    printIntro()

    n:int=getInputs()

    total:int=simNGames(n)
    
    report(total,n)

main()
