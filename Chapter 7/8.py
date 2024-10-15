# US Senate and House

def main()->None:

    age:int=int(input("Enter the person's age:"))
    years:int=int(input("Enter the years of citizenship:"))

    if age>=30 and years>=9:
        print("US Senator")
    elif age>=25 and years>=7:
        print("US House")
    else:
        print("Not eligible")


if __name__ == "__main__":
    main()

