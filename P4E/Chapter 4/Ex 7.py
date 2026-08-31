#using function
while(True):
    try:
        score = float(input("Enter a score between 0.0 and 1.0: "))
        break
    except:
        print("Bad Score, try again...")

def computegrade(suresh):
    if suresh >= 0.9:
        grade="A"
    elif suresh >=0.8:
        grade="B"
    elif suresh >=0.7:
        grade="C"
    elif suresh >=0.6:
        grade="D"
    else:
        grade="F"
    return(grade)

out=computegrade(score)
print(out)