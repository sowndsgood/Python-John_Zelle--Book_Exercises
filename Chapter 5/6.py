# Numeric Value for complete name
def main()->None:
    #User input for name
    name=input("Enter you name:")
    alphabets=' abcdefghijklmnopqrstuvwxyz'
    count=0
    for i in name:
        count=count+name.index(i)
    print("The count is:",count)
main()