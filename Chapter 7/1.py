#Company pay
hours:float=float(input("Input the number of hours worked:"))
rate:float=float(input("Input the hourly rate:"))
overtime_hours:float=hours-40
overtime_wage:float=rate*1.5
total:float=(hours*rate)+(overtime_hours*overtime_wage)
print("The total wages is:",total)