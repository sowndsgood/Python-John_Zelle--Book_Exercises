# Windchill Index

def main()->None:
    print(f"{'V,T':^10}",end=" ")
    for V in range(0,50,5):
        print(f"{V:^10}",end=" ")
    print("\n")
    for T in range(-20,60,10):
        print(f"{T:^10}",end=" ")
        for V in range(0,50,5):
            if V>3:
                ans=35.74+0.6215*T-35.75*(V**0.16)+0.4275*T*(V**0.16)
                answer=round(ans,2)
            else:
                answer='NA'

            print(f"{answer:^10}",end=" ")
        print('\n')

if __name__=='__main__':
    main()