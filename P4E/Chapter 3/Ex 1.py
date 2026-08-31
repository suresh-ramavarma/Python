hours= float(input("Enter number of hours :"))
rate=float(input("Enter hourly rate :"))
if hours>40:
    excess = hours-40
    pay = 40*rate + excess*rate*1.5
else:
    pay=hours*rate
print("The pay is :", pay)
