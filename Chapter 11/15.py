# List of Cards

from ex_6 import shuffle

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
        if self.rank in [1,2,3,4,5,6,7,8,9,10]:
            return self.rank
        elif self.rank in [11,12,13]:
            return 10

    def __str__(self):
        '''Returns a string that names the card.'''
        number:dict[int, str]={1:"Ace",11: "Jack",12: "Queen",13: "King"}
        type:dict[str,str]= {'s': "Spades",'d': "Diamonds",'c': "Clubs",'h': "Hearts"}

        return f"{number.get(self.rank, str(self.rank))} of {type[self.suit]}"
    
class Deck:

    def __init__(self):
        ''' Creates a new deck of 52 cards in a standard order'''
        self.cards = []
        for rank in range(1, 14):
            for suit in ['s', 'c', 'h', 'd']:
                card = Card(rank, suit)
                self.cards.append(card)
        
    def printCard(self):
        '''Print the names of cards'''
        for card in self.cards:
            print(card)

    def shuffle(self):
        '''Randomizes the order of the cards.'''
        shuffle(self.cards)

    def dealCard(self):
        '''Returns a single card from the top of the deck and removes the card from the deck.'''
        top_card = self.cards.pop()
        print(f'The removed card is: {top_card}')
        
    def cardsLeft(self):
        ''' Returns the number of cards remaining in the deck. '''
        return len(self.cards)

def main()->None:

    deck=Deck()

    deck.shuffle()

    deck.dealCard()

    print(f"Number of cards left:{deck.cardsLeft()}")

    deck.printCard()
    
main()