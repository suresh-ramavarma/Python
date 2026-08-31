total, count, average = [0, 0, 0]
while True:
    try:
        inp=input("Enter a number or type 'done': ")
        if inp != 'done':
            num=int(inp)
            count = count + 1
            total = total + num
        else:
            average = total/count
            print(total, count, average)
            break

    except:
        print("Invalid input")
