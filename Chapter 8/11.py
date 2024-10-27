# Heating and cooling degree days 

def main()->None:
    temp:list[str]=input("Enter the average daily temperatures:").split(",")
    temp:list[float]=[float(i) for i in temp]

    HDD=0
    CDD=0

    for i in temp:
        if i<60:
            HDD+=(60-i)
        if i>80:
            CDD+=(i-80)
    
    print(f"The running total of cooling and heating degree days is: {CDD},{HDD}")

if __name__=='__main__':
    main()