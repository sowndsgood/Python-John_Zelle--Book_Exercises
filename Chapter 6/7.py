#Compute the nth Fibonacci number (Programming Exercise 16 from Chapter 3.)

def fibonacci(n:int)->int:
    first=0
    second=1
    for i in range(n):
        new=first+second
        first=second
        second=new
    return new


def main()->None:
    n=int(input("Enter the number:"))
    print(f"The {n} th fibonacci number:{fibonacci(n)}")

main()