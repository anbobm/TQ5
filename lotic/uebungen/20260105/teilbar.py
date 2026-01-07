def teilbar(a, b):
    if a % b == 0:
        return True
    return False

for i in range(1, 21):
    divisor = 3
    is_divisible = teilbar(i, divisor)
    if is_divisible:
        print(f'{i} ist durch {divisor} ohne Rest teilbar')
        continue
    print(f'{i} ist durch {divisor} nicht ohne Rest teilbar')

for i in range(1, 21):
    divisor = 3
    is_divisible = teilbar(i, divisor)
    if is_divisible:
        print(i)
