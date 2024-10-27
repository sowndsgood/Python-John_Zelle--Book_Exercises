# Goldbach conjecture

from exercise_6 import prime_numbers_values

def main()->None:
    n:int=int(input("Enter a even number:"))
    if n%2==0:
        prime_numbers=prime_numbers_values(n)
        found=False
        for x in prime_numbers:
            for y in prime_numbers:
                if x+y==n:
                    print(x,y)
                    found=True
                    break
            if found:
                break
        
    else:
        print("Number is not even.")

main()