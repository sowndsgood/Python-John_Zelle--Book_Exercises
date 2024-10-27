# Syracuse or Collatz or Hailstone Sequence 

def main()->None:
    value:int=int(input("Enter the value:"))
    print("The sequence is:")
    list=[value]
    while(value!=1):
        if value%2==0:
            value=value/2
        else:
            value=3*value+1
        list.append(int(value))
    print(list)

if __name__=='__main__':
    main()