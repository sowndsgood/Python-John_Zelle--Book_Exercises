#Compares regular volleyball games to rally scoring

#importing random
from random import random

#printing introduction
def printIntro()->None:
    print('This program simulates a game of Volleyball and copmares with Rally Scoring. ')
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


#simulating one game (Normal Volleyball)
def simOneGame(a:float,b:float,game_type:str)->tuple[int,int]:
    scoreA:int=0
    scoreB:int=0

    server:str="A" 

    while not gameOver(scoreA,scoreB):
        if server=="A":
            if random()<a:
                scoreA+=1
            else:
                if game_type=='rally':
                    scoreB+=1
                server="B"
        else:
            if random()<b:
                scoreB+=1
            else:
                if game_type=='rally':
                    scoreA+=1
                server="A"
    return scoreA,scoreB

#simulating N games
def simNgames(a,b,n)->tuple[int,int,int,int]:
    winsAn:int=0
    winsBn:int=0
    winsAr:int=0
    winsBr:int=0
    for i in range(1,n+1): 

        scoreAn,scoreBn=simOneGame(a,b,'normal')
        if scoreAn>scoreBn:
            winsAn+=1
        else:
            winsBn+=1

        scoreAr,scoreBr=simOneGame(a,b,'rally')
        if scoreAr>scoreBr:
            winsAr+=1
        else:
            winsBr+=1
    return winsAn,winsBn,winsAr,winsBr 
        
#printing report for simulated games
def report(winsAn,winsBn,winsAr,winsBr,better_team)->None:
    perAn=winsAn/(winsAn+winsBn)*100
    perAr=winsAr/(winsAr+winsBr)*100
    perBn=winsBn/(winsAn+winsBn)*100
    perBr=winsBr/(winsAr+winsBr)*100
    
    print(f"{'Team':^20}|{'Team A':^10}|{'Team B':^10}")
    print(f"{'Normal Scoring':^20}|{perAn:^10.2f}|{perBn:^10.2f}")
    print(f"{'Rally Scoring':^20}|{perAr:^10.2f}|{perBr:^10.2f}")

    if better_team == 'A':
        ans:float = perAn - perAr
    elif better_team == 'B':
        ans:float = perBn - perBr
    if ans >= 0 and ans < 1: # assuming between 0-5% has no net advantage
        print(f"The better team {better_team} has no net advantage in both scorings.")
    elif ans >= 1:
        print(f"The better team {better_team} have more advantage in Normal scoring.")
    else:
        print(f"The better team {better_team} have reduced advantage in Normal scoring.")
        
#finding better team
def find_better_team(a:float,b:float)->str:
    if a>b:
        return 'A'
    elif b>a:
        return 'B'
    else:
        return 'Error'

#Main function
def main()->None:
    printIntro()
    while(True):
        a,b,n=getInputs()
        better_team:str=find_better_team(a,b)
        if better_team=='Error':
            print("Enter valid probabilties. They should not be same")
            continue
        else:
            break
    winsAn,winsBn,winsAr,winsBr=simNgames(a,b,n)
    report(winsAn,winsBn,winsAr,winsBr,better_team)

if __name__=='__main__':
    main()
