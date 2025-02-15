# List of Cards

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

def main()->None:

    input_file=input("Enter the file name:")
    infile=open(input_file,'r')

    cards=[]
    for line in infile:
        rank,suit=line.split()
        card=Card(rank,suit)
        cards.append(card)

    #cards.sort(key=Card.getRank)
    #cards.sort(key=Card.getSuit)

    cards.sort(key=lambda c:(c.getSuit(),c.getRank()))

    for card in cards:
        print(card)

    
main()