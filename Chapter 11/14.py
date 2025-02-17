# List of five cards as a Poker hand

class Card:
    def __init__(self, rank, suit):
        self.rank = int(rank)  # Ensure rank is stored as an integer
        self.suit = suit

    def getRank(self):
        '''Returns the rank of the card.'''
        return self.rank
    
    def getSuit(self):
        '''Returns the suit of the card.'''
        return self.suit

    def __str__(self):
        '''Returns a string that names the card.'''
        number = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        type = {'s': "Spades", 'd': "Diamonds", 'c': "Clubs", 'h': "Hearts"}
        return f"{number.get(self.rank, str(self.rank))} of {type[self.suit]}"

def RoyalFlush(cards):
    '''10, Jack, Queen, King, Ace, all of the same suit.'''
    suits = [card.getSuit() for card in cards]
    ranks = sorted([card.getRank() for card in cards])
    return ranks == [1, 10, 11, 12, 13] and all(suit == suits[0] for suit in suits)

def StraightFlush(cards):
    '''Five ranks in a row, all of the same suit.'''
    suits = [card.getSuit() for card in cards]
    ranks = sorted([card.getRank() for card in cards])
    return all(suit == suits[0] for suit in suits) and ranks == list(range(ranks[0], ranks[0] + 5))

def FourofKind(cards):
    '''Four of the same rank.'''
    ranks = [card.getRank() for card in cards]
    rank_counts = {rank: ranks.count(rank) for rank in ranks}
    return 4 in rank_counts.values()

def FullHouse(cards):
    '''Three of one rank and two of another.'''
    ranks = [card.getRank() for card in cards]
    rank_counts = {rank: ranks.count(rank) for rank in ranks}
    return sorted(rank_counts.values()) == [2, 3]

def Flush(cards):
    '''Five cards of the same suit.'''
    suits = [card.getSuit() for card in cards]
    return all(suit == suits[0] for suit in suits)

def Straight(cards):
    '''Five ranks in a row.'''
    ranks = sorted([card.getRank() for card in cards])
    return ranks == list(range(ranks[0], ranks[0] + 5))

def ThreeofKind(cards):
    '''Three of one rank (but not a full house or four of a kind).'''
    ranks = [card.getRank() for card in cards]
    rank_counts = {rank: ranks.count(rank) for rank in ranks}
    return 3 in rank_counts.values() and not FullHouse(cards) and not FourofKind(cards)

def TwoPair(cards):
    '''Two each of two different ranks.'''
    ranks = [card.getRank() for card in cards]
    rank_counts = {rank: ranks.count(rank) for rank in ranks}
    return list(rank_counts.values()).count(2) == 2

def Pair(cards):
    '''Two of the same rank (but not two pair, three or four of a kind).'''
    ranks = [card.getRank() for card in cards]
    rank_counts = {rank: ranks.count(rank) for rank in ranks}
    return 2 in rank_counts.values() and not TwoPair(cards) and not FourofKind(cards) and not ThreeofKind(cards)

def checkXHigh(cards):
    '''If none of the previous categories fit, X is the value of the highest rank.'''
    ranks = [card.getRank() for card in cards]
    highest_rank = max(ranks)
    rank_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    return f"{rank_names.get(highest_rank, str(highest_rank))} High"

def main():
    '''Reads the card data and determines the poker hand category.'''

    # Read input file containing cards
    with open("ex14_input.txt", 'r') as infile:
        cards = [Card(rank, suit) for rank, suit in (line.split() for line in infile)]

    # Sort first by rank, then by suit
    cards.sort(key=Card.getRank)
    cards.sort(key=Card.getSuit)

    # Display the sorted cards
    for card in cards:
        print(card)

    # Determine and print the hand category
    if RoyalFlush(cards):
        print("Category: Royal Flush")
    elif StraightFlush(cards):
        print("Category: Straight Flush")
    elif FourofKind(cards):
        print("Category: Four of a Kind")
    elif FullHouse(cards):
        print("Category: Full House")
    elif Flush(cards):
        print("Category: Flush")
    elif Straight(cards):
        print("Category: Straight")
    elif ThreeofKind(cards):
        print("Category: Three of a Kind")
    elif TwoPair(cards):
        print("Category: Two Pair")
    elif Pair(cards):
        print("Category: Pair")
    else:
        print(f"Category: {checkXHigh(cards)}")

if __name__ == "__main__":
    main()
