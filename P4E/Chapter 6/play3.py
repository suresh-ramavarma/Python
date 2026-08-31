while True:
    word=input("Enter a word (q to quit): ")
    if word.lower()=='q':
        break
    if word.lower()<'banana':
        print('Your word,' + word + ', comes before banana')
    elif word.lower()>'banana':
        print('Your word,' + word + ', comes after banana')
    else:
        print("All right, banana")