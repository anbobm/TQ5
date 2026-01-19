## 1. Maximum finden
```python
def maximum(liste):
    max_wert = liste[0]
    for x in liste:
        if x > max_wert:
            max_wert = x
    return max_wert
```

## 2. Minimum finden
```python
def minimum(liste):
    min_wert = liste[0]
    for x in liste:
        if x < min_wert:
            min_wert = x
    return min_wert
```

## 3. Summe berechnen
```python
def summe(liste):
    s = 0
    for x in liste:
        s += x
    return s
```

## 4. Anzahl positiver Zahlen
```python
def count_positive(liste):
    count = 0
    for x in liste:
        if x > 0:
            count += 1
    return count
```

## 5. Durchschnitt
```python
def durchschnitt(liste):
    return summe(liste) / len(liste)
```

## 6. Fakultät
```python
def fakultaet(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

## 7. Fibonacci
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
```

## 8. Teiler finden
```python
def teiler(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
```

## 9. Primzahlen bis n
```python
def primzahlen(n):
    for zahl in range(2, n + 1):
        ist_prim = True
        for i in range(2, zahl):
            if zahl % i == 0:
                ist_prim = False
                break
        if ist_prim:
            print(zahl)
```

## 10. Optimierter Primzahl-Test
```python
import math

def ist_primzahl(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

## 11. Duplikate entfernen
```python
def entferne_duplikate(liste):
    neu = []
    for x in liste:
        if x not in neu:
            neu.append(x)
    return neu
```

## 12. Häufigkeiten zählen
```python
def haeufigkeiten(liste):
    result = {}
    for x in liste:
        result[x] = result.get(x, 0) + 1
    return result
```

## 13. Zweitgrößte Zahl
```python
def zweitgroesste(liste):
    groesste = zweit = float('-inf')
    for x in liste:
        if x > groesste:
            zweit = groesste
            groesste = x
        elif x > zweit and x != groesste:
            zweit = x
    return zweit
```

## 14. Liste umdrehen
```python
def umdrehen(liste):
    neu = []
    for x in liste:
        neu.insert(0, x)
    return neu
```

## 15. Liste rotieren
```python
def rotieren(liste):
    return [liste[-1]] + liste[:-1]
```

## 16. Zeichen zählen
```python
def zeichen_zaehlen(text):
    result = {}
    for c in text:
        result[c] = result.get(c, 0) + 1
    return result
```

## 17. Vokale zählen
```python
def vokale_zaehlen(text):
    vokale = "aeiouAEIOU"
    count = 0
    for c in text:
        if c in vokale:
            count += 1
    return count
```

## 18. Wort umdrehen
```python
def wort_umdrehen(wort):
    neu = ""
    for c in wort:
        neu = c + neu
    return neu
```

## 19. Anagramm prüfen
```python
def anagramm(a, b):
    return sorted(a) == sorted(b)
```

## 20. Längstes Wort
```python
def laengstes_wort(text):
    woerter = text.split()
    max_wort = woerter[0]
    for w in woerter:
        if len(w) > len(max_wort):
            max_wort = w
    return max_wort
```

## 21. Ziffern ausgeben
```python
def ziffern(n):
    for c in str(n):
        print(c)
```

## 22. Dezimal zu Binär
```python
def dezimal_zu_binaer(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result
```

## 23. Binär zu Dezimal
```python
def binaer_zu_dezimal(b):
    result = 0
    for c in b:
        result = result * 2 + int(c)
    return result
```

## 24. Palindrom-Zahl
```python
def palindrom(n):
    s = str(n)
    return s == s[::-1]
```

## 25. Perfekte Zahl
```python
def perfekte_zahl(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
```

## 26. Lineare Suche
```python
def lineare_suche(liste, ziel):
    for i in range(len(liste)):
        if liste[i] == ziel:
            return i
    return -1
```

## 29. Duplikate finden
```python
def finde_duplikate(liste):
    seen = set()
    dup = set()
    for x in liste:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)
    return list(dup)
```

 