#  Racquetball Simulation

#importing random
from random import random

#printing introduction
def printIntro()->None:
    print('This program simulates a game of racquetball between two players called "A" and "B". ')
    print("The ability of each player is indicated by a probability (a number between 0 and 1) that the player wins the point when serving.") 
    print("First service alternates, so player A serves first in the odd games of the match, and player B serves first in the even games. ")

#getting inputs from user
def getInputs()->tuple[float,float,int]: 
    # Returns the three simulation parameters 
    a=float(input("What is the prob. player A wins a serve? (between 0 and 1) ")) 
    b=float(input("What is the prob. player B wins a serve? (between 0 and 1) ")) 
    n=int(input("How many games to simulate? ")) 
    return a, b, n 

#function to end game if game is over by checking scores
def gameOver(scoreA:int,scoreB:int)->bool:
    return scoreA==15 or scoreB==15

#simulating one game
def simOneGame(a:float,b:float,i:int)->tuple[int,int]:
    scoreA:int=0
    scoreB:int=0

    server="A" if i%2!=0 else "B"

    while not gameOver(scoreA,scoreB):
        if server=="A":
            if random()<a:
                scoreA+=1
            else:
                server="B"
        else:
            if random()<b:
                scoreB+=1
            else:
                server="A"
    return scoreA,scoreB

#simulating N games
def simNgames(a,b,n)->tuple[float,float]:
    winsA:int=0
    winsB:int=0
    for i in range(1,n+1): 
        scoreA,scoreB=simOneGame(a,b,i)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB

#printing report for simulated games
def report(winsA,winsB)->None:
    n = winsA + winsB 
    print("\nGames simulated:", n) 
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n)) 
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

#Main function
def main()->None:
    printIntro()
    a,b,n=getInputs()
    winsA,winsB=simNgames(a,b,n)
    report(winsA,winsB)

if __name__=='__main__':
    main()
