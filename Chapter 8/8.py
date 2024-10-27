# GCD Euclid's algorithm

def main()->None:
    m:int=int(input("Enter the number 1:"))
    n:int=int(input("Enter the number 2:"))

    while(m!=0):
        n,m=m,n%m
    
    print(f"The GCD is:{n}")

if __name__=='__main__':
    main()