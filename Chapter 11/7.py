# Inner product function

def innerProd(x,y):
    sum=0
    for i in range(len(x)):
        sum+=(x[i]*y[i])
    return sum

def main()->None:
    x=[2,3,4,5]
    y=[6,7,8,9]
    print(f"Inner Product of two lists: {innerProd(x,y)}")

main()
