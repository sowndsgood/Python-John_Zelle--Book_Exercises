#Solve Programming Exercise 17 from Chapter 3

import math

def nextGuess(guess:float,x:float)->float:
    nextguess=(guess+(x/guess))/2
    return nextguess

x:float=float(input("Enter the number:"))
guess:float=float(input("Enter current guess:"))
print(f"Guessed Answer:{nextGuess(guess,x):.3f}")
print(f"Closeness:{math.sqrt(x)-nextGuess(guess,x):.3f}")