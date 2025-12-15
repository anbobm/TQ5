start_price = 4.8
km = int(input('Bitte Kilometer eingegen: '))
if km > 5:
    costs = 1.9
else:
    costs = 2.1
total_expenses = start_price + costs * km
print("Deine Kosten sind:", total_expenses)