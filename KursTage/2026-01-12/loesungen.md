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
        s += x # s = s + x
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
def fakultaet(n): # 0! = 1
    result = 1
    for i in range(1, n + 1):
        result *= i # result = result * i
    return result
```

## 7. Fibonacci
```python
def fibonacci(n): # 0, 1, 1, 2, 3, 5, 8, 13, ..
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

# Variante ohne unpacking
def fibonacci(n): # 0, 1, 1, 2, 3, 5, 8, 13, ..
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        next = a + b
        a = b
        b = next
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

# Variante ohne get (man muss vorher nachsehen, ob Schlüssel im result vorhanden)
def haeufigkeiten(liste):
    result = {}
    for x in liste:
        if x in result:
            result[x] = result[x] + 1
        else:
            result[x] = 1
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
    letztes = liste[-1]
    liste_bis_letztes = liste[:-1]
    return [letztes] + liste_bis_letztes
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
        n //= 2   # n = n // 2
    return result
```

## 23. Binär zu Dezimal
```python
def binaer_zu_dezimal(b):   # 110101110
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
            s += i    # s = s + i
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

## 27. BubbleSort
Bubblesort ez (ohne Abkürzungen)
```python
def bubble_sort(liste):
    n = len(liste)

    for i in range(n):
        for j in range(0, n - 1):
            if liste[j] > liste[j + 1]:
                # j mit j + 1 tauschen
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
                # alternatives tauschen mit unpacking: a, b = b, a
                # liste[j], liste[j + 1] = liste[j + 1], liste[j]

    return liste
```

mit Vergleich immer nur bis zum `n-i`.ten Element:
```python
def bubble_sort(liste):
    n = len(liste)

    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # j mit j + 1 tauschen
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp

    return liste
```

mit Check ob Liste nach letztem Durchlauf bereits sortiert ist (keine Tauschung passiert):
```python
def bubble_sort(liste): # [5, 2, 4, 1, 0, 3]
    n = len(liste)

    for i in range(n):
        getauscht = False
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # j mit j + 1 tauschen
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
                
                getauscht = True
        if getauscht: break

    return liste
```

## 29. Duplikate finden
```python
def finde_duplikate(liste):
    gesehen = set()
    dup = set()
    for x in liste:
        if x in gesehen:
            dup.add(x) # { 3, 4} + {4} = {3, 4}
        else:
            gesehen.add(x)
    return list(dup)
```

