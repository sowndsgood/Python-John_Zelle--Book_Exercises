# Fuel Efficiency

def main()->None:
    start:int=int(input("Enter the starting odometer:"))
    odo=[]
    gas_read=[]
    MPG_leg=[]
    MPG=[]
    while(True):
        text=input("Enter the odometer reading and gas consumed:")
        if text=="":
            break

        try:
            odometer,gas=text.split()
            odometer=int(odometer)
            gas=int(gas)
            odo.append(odometer-start)
            gas_read.append(gas)
            MPG.append((odometer-start)/gas)
            start=odometer

        except ValueError:
            print("Enter valid values")
            break

    print("The MPG for each leg:",MPG)
    total_odo=sum(odo)
    total_gas=sum(gas_read)
    print("Total MPG:",total_odo/total_gas)

if __name__=="__main__":
    main()