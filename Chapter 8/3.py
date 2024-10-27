#Investment to double 

def main()->None:
    interest:float=float(input("Enter the interest rate:"))
    amount:float=float(input("Enter the initial:"))
    years:int=0
    target=2*amount
    final:float=amount
    while True:
        final*=(1+(interest/100))
        if final>=target:break
        years+=1

    print("Years taken is:",years)

if __name__=='__main__':
    main()