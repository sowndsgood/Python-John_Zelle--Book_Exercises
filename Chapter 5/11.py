# Improved version of the chaos . py program from Chapter 1
def main()->None: 

    print("This program illustrates a chaotic function") 

    #Input from user
    x:float = float(input("Enter first number between 0 and 1: "))
    y:float = float(input("Enter second number between 0 and 1: "))
    z:int=int(input("Enter number of iterations:"))

    #Table printing
    print("index      {0}       {1}".format(x,y))
    for i in range(z): 
        a:float=3.9*x*(1-x)
        b:float=3.9*y*(1-y)
        print("{0:^6}   {1:8.6f}    {2:8.6f}".format(i,a,b))
        x:float=a
        y:float=b

main()