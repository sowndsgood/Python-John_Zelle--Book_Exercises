#Leap Year or not

def main()->None:
    year:int=int(input("Enter the year:"))

    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Non Leap Year")
    else:
        if year%4==0:
            print("Leap year")
        else:
            print("Non Leap Year")

main()

""" 

BETTER SOLUTION

if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap Year")
else:
    print("Non Leap Year")

"""