# Sorry! Game

from random import randint

def main():

    players=["Player 1","Player 2"]
    score={"Player 1":0,"Player 2":0}
    target=30

    while True:
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            point=randint(1,6)
            print(f"{player} rolled a {point}!")

            if target>= score[player]+point:
                score[player]+=point
            print(f"{player} is now at position {score[player]}.")

            if score[player]==target:
                print(f"{player} wins!")
                return
            
            opponent=players[1] if player==players[0] else players[0]
            if score[player]==score[opponent] and score[player]!=0:
                score[opponent]=0

main()