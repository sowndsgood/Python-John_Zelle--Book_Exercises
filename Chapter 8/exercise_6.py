# Every prime number

from exercise_5 import prime

def prime_numbers_values(n):
    prime_numbers:list[int]=[]
    for i in range(2,n+1):
        if prime(i):
            prime_numbers.append(i)
    return prime_numbers

def main()->None:
    n:int=int(input("Enter the number:"))
    print(prime_numbers_values(n))   

if __name__=='__main__':
    main()