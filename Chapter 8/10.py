# Fuel Efficiency

def main()->None:
    file=input("Enter the file name:")
    content=open(file,'r')
    start:int=int(content.readline())
    odo=[]
    gas_read=[]
    MPG_leg=[]
    MPG=[]
    while(True):
        text=content.readline()
        if text=="":
            break

        try:
            odometer,gas=text.split()
            odometer=int(odometer)
            gas=int(gas)
            odo.append(odometer-start)
            gas_read.append(gas)
            MPG.append(round((odometer-start)/gas,2))
            start=odometer

        except ValueError:
            print("Enter valid values")
            break

    print("The MPG for each leg:",MPG)
    total_odo=sum(odo)
    total_gas=sum(gas_read)
    print("Total MPG:",round(total_odo/total_gas,2))

if __name__=="__main__":
    main()