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
    try:
        n=int(input("Enter the number:"))
        if n<0:
            raise ValueError("Negative Number not allowed")
        
        print(f"The {n} th fibonacci number:{fibonacci(n)}")
    except ValueError as err:
        if "invalid literal for int() with base 10: " in str(err):
            print("Not an number")
        else:
            print(err)
    

main()