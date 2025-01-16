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
            
def simOneGame(start:int)->bool:
    hasAce:bool=start==1
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


def simNGames(n:int)->list[float]:
    prob:list=[]

    for start in range(1,11):
        busts=sum(simOneGame(start) for _ in range(n))
        prob.append(busts/n)

    return prob

#Report
def report(prob:list[float])->None:
    for i,bust in enumerate(prob):
        print(f"Starting Card:{'Ace'if i==0 else str(i+1)} Bust Probability:{bust:.4f}")

def main()->None:
    printIntro()

    n:int=getInputs()

    prob:list=simNGames(n)
    
    report(prob)

main()