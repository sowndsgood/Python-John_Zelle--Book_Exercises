#Crazy Eights

import random

def is_playable(card,top_card):
    #play only if there is match of the top card’s rank or suit or an 8
    return card.split()[0]=='8' or card.split()[0]==top_card.split()[0] or card.split()[1]==top_card.split()[1]

def main():

    ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits=['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck=[f"{rank} of {suit}" for rank in ranks for suit in suits]

    player_cards=[deck.pop() for i in range(5)]
    computer_cards=[deck.pop() for i in range(5)]
    top_card=deck.pop()

    print(f"Starting Card is: {top_card}")

    while True:
        print("\nYour hand:", player_cards)
        print("Top card:", top_card)

        playable = [card for card in player_cards if is_playable(card, top_card)]
        if playable:
            choice = input(f"Play one: {playable} or type 'draw': ")
            if choice == 'draw':
                if deck:
                    player_cards.append(deck.pop())
                else:
                    print("Deck empty! Skipping turn.")
            elif choice in playable:
                player_cards.remove(choice)
                top_card = choice
                if not player_cards:
                    print("You win!")
                    break
        else:
            print("No playable cards. Drawing...")
            if deck:
                player_cards.append(deck.pop())

        # Computer's turn
        computer_playable = [card for card in computer_cards if is_playable(card, top_card)]
        if computer_playable:
            comp_card = random.choice(computer_playable)
            computer_cards.remove(comp_card)
            top_card = comp_card
            print(f"Computer played: {comp_card}")
            if not computer_cards:
                print("Computer wins!")
                break
        else:
            print("Computer draws a card.")
            if deck:
                computer_cards.append(deck.pop())

if __name__=='__main__':
    main()