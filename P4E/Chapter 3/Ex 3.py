while(True):
    try:
        score = float(input("Enter a score between 0.0 and 1.0: "))
        break
    except:
        print("Bad Score, try again...")

if score >= 0.9:
    grade="A"
elif score >=0.8:
    grade="B"
elif score >=0.7:
    grade="C"
elif score >=0.6:
    grade="D"
else:
    grade="F"
print(grade)