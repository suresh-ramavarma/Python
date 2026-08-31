largest=None
print("Before: ", largest)
for i in [3, 41, 12, 9, 74, 15]:
    if largest is None or i > largest:
        largest = i
    print('Loop ', i, largest)
print('Largest ', largest)