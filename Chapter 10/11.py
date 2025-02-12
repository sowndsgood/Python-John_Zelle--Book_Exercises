# Class for playing cards

from typing import Dict

from random import randint,choice

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        '''Returns the rank of the card.'''
        return self.rank
    
    def getSuit(self):
        '''Returns the suit of the card.'''
        return self.suit
    
    def value(self):
        '''Returns the Blackjack value of a card.'''
        if self.rank == 1:
            return 1
        elif self.rank in [2,3,4,5,6,7,8,9,10]:
            return self.rank
        elif self.rank in [11,12,13]:
            return 10

    def __str__(self):
        '''Returns a string that names the card.'''
        number:Dict[int, str]={1:"Ace",11: "Jack",12: "Queen",13: "King"}
        type:dict[str,str]= {'s': "Spades",'d': "Diamonds",'c': "Clubs",'h': "Hearts"}

        return f"{number.get(self.rank, str(self.rank))} of {type[self.suit]}"

def main()->None:

    n:int=int(input("Enter number of times to generate cards at random:"))

    for i in range(n):
        rank:int=randint(1,13)
        suit:str=choice(['s','h','c','d'])
        card=Card(rank,suit)
        #print(f"The card rank and suit are:{card.getRank()},{card.getSuit()}")
        print(f"Card is {card} and blackjack value is:{card.value()}")

main()