# Modify 9th problem range

from exercise_9 import find_value

def main()->None:
    year:int=int(input("Enter a year from 1900-2099:"))
    
    if 1900>year or year>2099:
        print("Enter a valid year")
    else:
        date=22
        sum=find_value(year)
        if year in [1954,1981,2049,2076]:
            date-=7
        
        if 0<=sum <=9:
            date+=(sum)
            print(f"The date is: March {date}")
        else:
            date=(sum)-9
            print(f"The date is: April {date}")
            
main()