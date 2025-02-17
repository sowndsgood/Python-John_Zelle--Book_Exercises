import random

cards= {'A': 4, 'K': 3, 'Q': 2, 'J': 1, 'T': 0}

ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits=['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck=[f"{rank} of {suit}" for rank in ranks for suit in suits]

random.shuffle(deck)
hands=[deck[i:i + 13] for i in range(0, 52, 13)]

def calculate_points(hand):
    points = 0
    for card in hand:
        rank = card.split()[0]  
        points += cards.get(rank, 0) 
    return points

def opening_bid(points):
    if points <= 7:
        return "Pass"
    elif 8 <= points <= 11:
        return "1NT"
    elif 12 <= points <= 15:
        return "1"
    elif 16 <= points <= 18:
        return "2"
    else:
        return "3 or higher"

for i, hand in enumerate(hands):
    print(f"Player {i + 1}'s Hand: {hand}")
    points = calculate_points(hand)
    bid = opening_bid(points)
    print(f"Total Points: {points}")
    print(f"Opening Bid: {bid}\n")
