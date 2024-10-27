# Prime Number or not

import math

def prime(n):
    list=[i for i in range(2,int(math.sqrt(n))+1)]
    for i in list:
        if n%i==0:
            return False
        
    return True
    
def main()->None:
    n:int=int(input("Enter the number:"))
    if prime(n):
        print("Prime")
    else:
        print("Not prime")

if __name__=='__main__':
    main()