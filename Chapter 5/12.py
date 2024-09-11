# Improved version of the futval.py program from Chapter 2
def main()->None: 

    print("This program calculates the future value of investment.") 

    #Input from user
    principal:float = eval(input("Enter the initial principal: ")) 
    apr:float = eval(input("Enter the annual interest rate: ")) 
    years:float = eval(input("Enter the  the number of years: "))

    #Table printing
    print("Year       Value")
    for i in range(years): 
        principal=principal * (1 + apr/100) 
        print("{0:^6}   ${1:6.2f}".format(i,principal)) 

main()