#Tennis Game

from random import random

class Player:

    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        self.games = 0
        self.sets = 0
        self.matches = 0

    def wins_serve(self):
        return random() <= self.prob

    def increment_score(self):
        self.score += 1

    def increment_games(self):
        self.games += 1
        self.score = 0  

    def increment_sets(self):
        self.sets += 1
        self.games = 0  

    def increment_matches(self):
        self.matches += 1
        self.sets = 0  

class TennisMatch:
    
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA  

    def play_game(self):
        while not self.is_game_over():
            if self.server.wins_serve():
                self.server.increment_score()
            else:
                self.get_opponent(self.server).increment_score()

        if self.playerA.score > self.playerB.score:
            self.playerA.increment_games()
        else:
            self.playerB.increment_games()

        self.switch_server()

    def is_game_over(self):
        a, b = self.playerA.score, self.playerB.score
        return (a >= 4 or b >= 4) and abs(a - b) >= 2

    def play_set(self):
        while not self.is_set_over():
            self.play_game()

        if self.playerA.games > self.playerB.games:
            self.playerA.increment_sets()
        else:
            self.playerB.increment_sets()

    def is_set_over(self):
        a, b = self.playerA.games, self.playerB.games
        return (a >= 6 or b >= 6) and abs(a - b) >= 2

    def play_match(self):
        while not self.is_match_over():
            self.play_set()

        if self.playerA.sets > self.playerB.sets:
            self.playerA.increment_matches()
        else:
            self.playerB.increment_matches()

    def is_match_over(self):
        return self.playerA.sets == 2 or self.playerB.sets == 2

    def switch_server(self):
        self.server = self.get_opponent(self.server)

    def get_opponent(self, player):
        return self.playerA if player == self.playerB else self.playerB

    def get_winner(self):
        return "A" if self.playerA.matches > self.playerB.matches else "B"

class MatchStats:
    
    def __init__(self):
        self.winsA = 0
        self.winsB = 0

    def update(self, match):
        if match.get_winner() == "A":
            self.winsA += 1
        else:
            self.winsB += 1

    def print_report(self):
        total_matches = self.winsA + self.winsB
        print("\nSummary of", total_matches, "matches:")
        print("Player A Wins:", self.winsA, f"({self.winsA / total_matches:.1%})")
        print("Player B Wins:", self.winsB, f"({self.winsB / total_matches:.1%})")

def print_intro():

    print("This program simulates tennis matches between two players, A and B.")
    print("Each player has a probability of winning a point on their serve.")
    print("Matches are played in a best-of-3 sets format.")

def get_inputs():

    probA = float(input("Enter the probability of player A winning a point: "))
    probB = float(input("Enter the probability of player B winning a point: "))
    num_matches = int(input("Enter the number of matches to simulate: "))
    return probA, probB, num_matches

def main():
    
    print_intro()
    probA, probB, num_matches = get_inputs()
    
    stats = MatchStats()

    for i in range(num_matches):
        match=TennisMatch(probA, probB)
        match.play_match()
        stats.update(match)
    
    stats.print_report()

    while True:
        key = input("\n Press Enter to simulate again or type 'q' to quit: ")
        if key.lower() == 'q':
            break
        main()

if __name__ == "__main__":
    main()