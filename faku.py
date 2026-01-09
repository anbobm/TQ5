def fakultaet(n):
    if n < 0:
        raise ValueError("Fakultät ist nur für nicht-negative Zahlen definiert")
    
    ergebnis = 1
    for i in range(1, n + 1):
        ergebnis *= i
    return ergebnis

# Beispiele
print(fakultaet(0))  # 1
print(fakultaet(1))  # 1
print(fakultaet(5))  # 120
print(fakultaet(10)) # 3628800
print(fakultaet(15)) # 1307674368000