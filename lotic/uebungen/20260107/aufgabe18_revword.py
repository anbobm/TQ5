example_string = 'donnerwetter'
reverse_string = ''

for i in range (len(example_string)-1, -1, -1):
    reverse_string += example_string[i]

print(reverse_string)
