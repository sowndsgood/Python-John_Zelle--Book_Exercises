# Fibonacci Sequence

def main()->None:
    n:int=int(input("Enter the value of n:"))

    first=0
    second=1
    ans=[1]
    for i in range(0,n):
        present=first+second
        first=second
        second=present
        ans.append(present)
    print(ans[n-1])

main()

