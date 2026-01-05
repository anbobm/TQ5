from random import randint

# Create new list
mylist = []

# Fill list with 20 random integers ranging from 1-50
for i in range(0, 20):
    mylist.append(randint(1, 50))

# Print unsorted list
print('Zufällig erzeugte liste')
print(mylist)

# Create a set out of our list to filter out duplicates 
myset = set()
myset.update(mylist)

# Convert set back to list. 
clean_list = list(myset)
# and sort it.
clean_list.sort()

print(f'{len(mylist) - len(clean_list)} Duplikate entfernt')
print(clean_list)

