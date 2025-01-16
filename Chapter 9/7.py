# Craps Simulation

#importing random
from random import randint
    
#printing introduction
def printIntro()->None:
    print('This program simulates a game of Craps. We have to specify the number of games to simulate. ')
    print("The  probability of winning the game is displayed.") 

#getting inputs from user
def getInputs()->int: 
    n:int=int(input("Enter the number of games:"))
    return n 

#Function for Initial Roll
def initial_roll()->tuple[str,int]:
    roll:int=randint(1,6)+randint(1,6)

    if roll in [2,3,12]: return roll,'Loss'
    elif roll in [7,11]: return roll, 'Win'
    else: return roll, 'Point'


def point_roll(point:int)->int:
    while True:
        point:int=0
        res=randint(1,6)+randint(1,6)
        if res==point:
            point=1
            break
        elif res==7:
            break

    return point

#simulating one game
def simOneGame()->int:
    point,result=initial_roll()
    if result=='Win': return 1
    elif result=='Loss': return 0
    elif result=='Point': return point_roll(point)

#simulating N games
def simNgames(n:int)->int:
    total:int=0
    for i in range(n):
        total+=simOneGame()
    return total

#Report
def report(total:int,n:int)->None:
    print(f"Total games won:{total}")
    print(f"Probability of winning: {total/n:.4f}")
    print(f"Percentage of winning: {total*100/n:.4f} %")

def main()->None:
    printIntro()

    n:int=getInputs()

    total=simNgames(n)

    report(total,n)

main()
