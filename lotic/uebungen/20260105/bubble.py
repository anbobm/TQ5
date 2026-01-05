from random import randint

# Create new list
mylist = []

# Fill list with 20 random integers ranging from 1-100
for i in range(0, 20):
    mylist.append(randint(1, 100))

# Print unsorted list
print(mylist)

# Bubblesort
max_index = len(mylist) - 1
while max_index > 0:
    for i in range(0, max_index + 1):
        number1 = mylist[i]
        if i + 1 > max_index:
            break
        number2 = mylist[i+1]
        if number1 > number2:
            mylist[i] = number2
            mylist[i+1] = number1
    max_index -= 1

#Print sorted list
print(mylist)

