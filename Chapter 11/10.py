# Sieve of Eratosthenes

def seive(n):

    list=[i for i in range(2,n+1)]
    prime=[]

    while list:
        first=list[0]
        prime.append(first)
        list.remove(first)

        for i in list:
            if i%first==0:
                list.remove(i)

    return prime

def main()->None:

    n:int=int(input("Enter the number:"))

    print(f"The prime numbers include:{seive(n)}")

main()