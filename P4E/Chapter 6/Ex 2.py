def counter(myword, myletter):
    count=0
    for i in myword:
        if i == myletter:
            count=count+1
    return(count)


word=input("Enter a word: ")
while True:
    letter = input("Which letter do you want to find? ")
    if len(letter)!=1:
        print("Please enter only one letter")
    else:
        break
word=word.lower()
letter=letter.lower()
count=counter(word,letter)
print(letter, "apprears in", word, count, "times.")
