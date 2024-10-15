#College Classification

def main()->None:
    credits=int(input("Enter the number of credits:"))

    classification=""
    if credits>=26:
        classification="Senior"
    elif credits>=16:
        classification="Junior"
    elif credits>=7:
        classification="Sophomore"
    elif credits<7:
        classification="Freshman"

    print("The classification is:",classification)


main()