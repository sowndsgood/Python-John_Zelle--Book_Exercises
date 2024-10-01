#List of Strings to  List of Number

def toNumbers(strList:list[str])->None:

    for i,element in enumerate(strList):
        strList[i]=int(strList[i])

def main()->None:
    string:str=(input("Enter the numbers separated by comma:"))
    strList=string.split(",")

    type_before_function:list[str]=[type(i) for i in strList]
    print(f"Type before convertion:{type_before_function}")

    toNumbers(strList)
    print(f"The new list is:{strList}")

    type_after_function:list[str]=[type(i) for i in strList]
    print(f"Type after convertion:{type_after_function}")

main()