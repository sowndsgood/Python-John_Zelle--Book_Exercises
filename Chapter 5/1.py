# Program that converts a date in form "mm./dd/yyyy" to "month day, year" 
def main()-> None: 
    dateStr:str= input("Enter a date (mm/dd/yyyy) : ") 
    monthStr, dayStr, yearStr = dateStr.split("/")  #can't declare typehints separately for each variable while unpacking
    months:list[str] = ["January", "February", "March", "April", "May", "June" , "July" , "August" , "September", "October", "November", "December"]
    monthStr:str = months[int(monthStr)-1] 
    print("The converted date is: {0} {1:0>2},{2}".format(monthStr,dayStr,yearStr)) 

main()