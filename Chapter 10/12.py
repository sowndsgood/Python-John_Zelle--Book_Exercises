# Displaying 5 random Cards

from graphics import *
from random import randint, choice

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if self.rank == 1:
            return 1
        elif self.rank in range(2,11):
            return self.rank
        elif self.rank in range(11,14):
            return 10
        
    def __str__(self):
        dict1 = {
            1:"Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        dict2 = {
            's': "Spades",
            'd': "Diamonds",
            'c': "Clubs",
            'h': "Hearts"
        }

        return dict1.get(self.rank, str(self.rank)).lower() + "_of_" + dict2.get(self.suit).lower()
    
def main()->None:

    win = GraphWin("Random Cards", 1000, 600)

    rank = randint(1,13)
    suit = choice(['s', 'h', 'c', 'd'])

    for i in range(5):
        
        card = Card(rank, suit)

        card_file=card+".gif"

        image = Image(Point(500, 300),card_file)
        image.draw(win)

        time.sleep(5)
        image.undraw()

main()