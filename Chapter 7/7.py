# Babysitter Bill

def main()->None:
    start=input("Enter the starting time in hours:minutes (24 hour format) :")
    end=input("Enter the ending time in hours:minutes (24 hour format):")
    start_hour,start_min=start.split(":")
    end_hour,end_min=end.split(":")
    start_time=int(start_hour)+int(start_min)/60
    end_time=int(end_hour)+int(end_min)/60
    if start_time<21 and end_time<21:
        hour=end_time-start_time
        fare=2.50*hour
    elif start_time<21 and end_time>=21:
        normal=21-start_time
        low=end_time-21
        fare=2.50*normal+1.75*low
    else:
        hour=end_time-start_time
        fare=1.75*hour

    print(f"The fare is: ${fare:.2f}")


main()