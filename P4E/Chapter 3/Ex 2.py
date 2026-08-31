while(True):
    try:
        hours= float(input("Enter number of hours :"))
        rate=float(input("Enter hourly rate :"))
    except:
        print("Please enter a numeric value")

if hours>40:
    excess = hours-40
    pay = 40*rate + excess*rate*1.5
else:
    pay=hours*rate
print("The pay is :", pay)