#program to prompt list of numbers and print min and max
mini, maxi = [None, None]
while True:
    try:
        inp=input("Enter a number or type 'done': ")
        if inp != 'done':
            num=int(inp)
            if maxi is None or num > maxi:
                maxi = num
            if mini is None or num < mini:
                mini = num
        else:
            print(maxi, mini)
            break

    except:
        print("Invalid input")
