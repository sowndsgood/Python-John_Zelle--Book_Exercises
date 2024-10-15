#BMI Message

import math  #Math Library

def main()->None:
    weight:float=float(input("Enter the person's weight in pounds:"))
    height:float=float(input("Enter the person's height in cm:"))
    BMI:float=(weight*720)/math.pow(height,2)

    if BMI>=19 and BMI <=25:
        print("Healthy")
    elif BMI<19:
        print("Below BMI Range")
    elif BMI>25:
        print("Above BMI Range")

main()