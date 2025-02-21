# Recursive Function for Base Conversion

def baseConversion(num, base):

    temp=num%base
    num=num//base

    print(num,temp)

    if num==0:
        return 0
    if num<base:
        temp=num
        num=0
        print(num,temp)
    else:
        baseConversion(num,base)

def main()->None:

    num:int=int(input("Enter the number:"))
    base:int=int(input("Enter the base:"))
    baseConversion(num, base)

main()