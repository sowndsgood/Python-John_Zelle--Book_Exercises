def main():
    print("MONTH NAME\n")
    num=int(input("Enter the month number:"))
    position=(num-1)*3
    month="JanFebMarAprMayJunJulAugSepOctNovDec"
    print("The month name:",month[position:position+3])

main()