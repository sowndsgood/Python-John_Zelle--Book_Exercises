#Speeding Ticket Fine Policy

def main()->None:
    
    limit:float=float(input("Enter the speed limit:"))
    speed:float=float(input("Enter the speed:"))

    if speed<=limit:
        print("The speed was legal")
    else: 
        extra=speed-limit
        fine=50+extra*5
        if speed>90:
            fine+=200
        
        print(f"The fine with penalty is:{fine:.2f}")

main()