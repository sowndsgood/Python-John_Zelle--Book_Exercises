#Greed Dice Game

from random import randint

def roll_dice():
    return [randint(1,6) for i in range(6)]

def calculate_points(dice):
    score=0

    counts={i:dice.count(i) for i in range(1,7)}

    score+=counts[1]*100
    score+=counts[5]*50

    for i,count in counts.items():
        if count>=3:
            if i==1:
                score+=1000
            else:
                score+=i*100

    return score

def main():

    total_score=0

    play=True

    while play:
        print(f"Your current total score: {total_score}")

        dice=roll_dice()
        print(f"You rolled:{dice}")

        score=calculate_points(dice)
        if score==0:
            print("No score in this roll. You lose all points for this round!")
            total_score = 0
        else:
            print(f"You scored {score} points this round.")
            total_score += score

        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice != 'y':
            play=False
            
        print(f"\nGame Over! Your total score is {total_score}")
main()