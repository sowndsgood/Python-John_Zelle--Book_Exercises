# Numeric Value for Name
def main()->None:
    #User input for name
    name=input("Enter the name:")
    #Converting to lower case
    name=name.lower()
    alphabets="abcdefghijklmnopqrstuvwxyz"
    count=0
    for i in name:
        print(i)
        a=alphabets.index(i) + 1
        count+=a
    print("The count is:{}".format(count))
main()