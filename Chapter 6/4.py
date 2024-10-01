#Function Definitions

def sumN(n)->int:
    return n*(n+1)//2

def sumNCubes(n)->int:
    return (n*(n+1)//2)**2


def main()->None:
    n:int=int(input("Enter the number n:"))
    print(f"The sum of the first n natural numbers is: {sumN(n)}")
    print(f"The sum of the cubes of the first n natural numbers is:{sumNCubes(n)}")

main()