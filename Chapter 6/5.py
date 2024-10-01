# Redo Programming Exercise 2 from Chapter 3

# Write a program that calculates the cost per square inch of a circular pizza, 
#given its diameter and price. The formula for area is A = 1rr2• 

import math

def area_of_pizza(diameter)->float:
    radius=diameter/2
    return math.pi*radius*radius

def cost_per_square_inch(area,cost)->float:
    return cost/area

def main()->None:
    diameter:float=float(input("Enter diameter of pizza:"))
    cost:float=float(input("Enter the cost of pizza:"))

    print(f"The cost per square inch of a circular pizza is: {cost_per_square_inch(area_of_pizza(diameter),cost):.4f}")

main()
