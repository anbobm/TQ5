number = 1024 
remaining = number
binary = ''
div = 2

while number % div != number:
    div *= 2

while div > 1:
    div /= 2
    if remaining % div != remaining:
        binary += '1'
        remaining = remaining % div
        continue
    binary += '0'

print(binary)
