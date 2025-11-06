# Finde die Summe aller Zahlen bis 1000, die ein Vielfaches von 3 oder 5 sind

multipleSum = 0

for i in range (1, 1000):
  if i % 3 == 0 or i % 5 == 0:
    multipleSum += i
    # multipleSum = multipleSum + i

print(f'Summe: {multipleSum}')