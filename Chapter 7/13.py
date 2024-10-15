# Day Number

def main()->None:
    date=input("Enter the date as month/day/year:")
    list1:list=date.split("/")
    month,day,year=[int(i) for i in list1] #List Comprehension

    dayNum:int=31*(month-1)+day
    if month>2:
        dayNum-=(4*month+23)//10
    if (year%400==0) or (year%4==0 and year%100!=0):
        dayNum+=1

    print(f"It is {dayNum}th day")

main()