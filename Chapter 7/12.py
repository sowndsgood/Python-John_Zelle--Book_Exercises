# Valid Date or not

def main()->None:
    date:str=input("Enter the date in form of month/day/year:")
    month,day,year=date.split("/")
    month=int(month)
    day=int(day)
    year=int(year)
    days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    ans="Invalid"
    if 1<=month<=12:
        if ((year%4==0 and year%100!=0) or (year%400==0)) and month==2:
            if day<=(days[2]+1):
                    ans="Valid"
        else:
            if 1<=day<=days[month]:
                ans="Valid"

    print(ans)

main()