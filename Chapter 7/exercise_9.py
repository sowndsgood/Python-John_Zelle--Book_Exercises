#Easter Date 

def find_value(year:int)->int:
    a:int=year%19
    b:int=year%4
    c:int=year%7
    d:int=(19*a+24)%30
    e:int=(2*b+4*c+6*d+5)%7
    return d+e

def main()->None:

    year:int=int(input("Enter a year from 1982 -2048:"))
    

    if 1982 <= year <=2048:
        date=22
        if 0<=sum <=9:
            date+=(sum)
            print(f"The date is: March {date}")
        else:
            date=(sum)-9
            print(f"The date is: April {date}")
    else:
        print("Enter a valid year")


if __name__=="__main__":
    main()

'''
BETTER SOLUTION
(22+d+e)%31 for April
'''