from random import random, choice

# Function to check if the match is over (best of 5 games)
def matchOver(gamesA: int, gamesB: int) -> bool:
    return gamesA == 3 or gamesB == 3

# Function to check if a game is over
def gameOver(scoreA: int, scoreB: int) -> bool:
    return (scoreA >= 11 or scoreB >= 11) and abs(scoreA - scoreB) >= 2

# Function to simulate a single game
def simOneGame(probA: float, probB: float, serving: str) -> str:
    scoreA = 0
    scoreB = 0
    serveSwitch = 0  # to switch serve every 2 points

    while not gameOver(scoreA, scoreB):
        if serveSwitch == 2:  # Switch serve every 2 points
            serving = 'A' if serving == 'B' else 'B'
            serveSwitch = 0
        
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
        else:
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1
        
        serveSwitch += 1

    return 'A' if scoreA > scoreB else 'B'

# Function to simulate a match (best of 5 games)
def simMatch(probA: float, probB: float) -> str:
    gamesA = 0
    gamesB = 0
    serving = choice(['A', 'B'])  # Randomly decide who serves first

    while not matchOver(gamesA, gamesB):
        winner = simOneGame(probA, probB, serving)
        if winner == 'A':
            gamesA += 1
        else:
            gamesB += 1

    return 'A' if gamesA > gamesB else 'B'

# Function to simulate multiple matches
def simNMatches(probA: float, probB: float, n: int) -> tuple[int, int]:
    winA = 0
    winB = 0
    for _ in range(n):
        winner = simMatch(probA, probB)
        if winner == 'A':
            winA += 1
        else:
            winB += 1

    return winA, winB

# Function to print introduction
def intro() -> None:
    print("This program simulates a table tennis match.")
    print("It simulates a best-of-5 games match with probabilities for each player to win a point.")
    print("The simulation will estimate the probability of each player winning a match.")

# Function to get user inputs
def getInputs() -> tuple[float, float, int]:
    probA = float(input("Enter the probability that player A wins a point: "))
    probB = float(input("Enter the probability that player B wins a point: "))
    n = int(input("Enter the number of matches to simulate: "))
    return probA, probB, n

# Function to report the simulation results
def report(winsA: int, winsB: int, n: int) -> None:
    print(f"Total matches simulated: {n}")
    print(f"Player A wins: {winsA} ({winsA/n * 100:.2f}%)")
    print(f"Player B wins: {winsB} ({winsB/n * 100:.2f}%)")

# Main function
def main() -> None:
    intro()
    probA, probB, n = getInputs()
    winsA, winsB = simNMatches(probA, probB, n)
    report(winsA, winsB, n)

main()
