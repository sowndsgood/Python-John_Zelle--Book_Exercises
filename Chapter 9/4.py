# Rally Scoring

#importing random
from random import random

#printing introduction
def printIntro()->None:
    print('This program simulates a game of Volleyball using Rally Scoring. ')
    print("The ability of each team is indicated by a probability (a number between 0 and 1) that the team wins the point when serving.") 

#getting inputs from user
def getInputs()->tuple[float,float,int]: 
    # Returns the three simulation parameters 
    a=float(input("What is the prob. team A wins a serve? (between 0 and 1): ")) 
    b=float(input("What is the prob. team B wins a serve? (between 0 and 1): ")) 
    n=int(input("How many games to simulate? ")) 
    return a, b, n 

#function to end game if game is over by checking scores
def gameOver(scoreA:int,scoreB:int)->bool:
    return (scoreA>=25 or scoreB>=25) and abs(scoreA-scoreB)>=2


#simulating one game
def simOneGame(a:float,b:float)->tuple[int,int]:
    scoreA:int=0
    scoreB:int=0

    server:str="A" 

    while not gameOver(scoreA,scoreB):
        if server=="A":
            if random()<a:
                scoreA+=1
            else:
                scoreB+=1
                server="B"
        else:
            if random()<b:
                scoreB+=1
            else:
                scoreA+=1
                server="A"
    return scoreA,scoreB

#simulating N games
def simNgames(a,b,n)->tuple[int,int]:
    winsA:int=0
    winsB:int=0
    for i in range(1,n+1): 
        scoreA,scoreB=simOneGame(a,b)
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