#Using functions to solve Programming Exercise 1 from Chapter 3

import math

def sphereArea(radius)->float:
    return (4*math.pi*radius*radius*radius)/3

def sphereVolume(radius)->float:
    return 4*math.pi*radius*radius

def main()->None:
    radius:float=float(input("Enter the radius:"))
    print(f"The surface area of sphere is:{sphereArea(radius):.4f}")
    print(f"The volume of sphere is: {sphereVolume(radius):.4f}")

main()