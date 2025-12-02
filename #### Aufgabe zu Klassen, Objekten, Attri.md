#### Aufgabe zu Klassen, Objekten, Attributen und Methoden

Schreibe eine Klasse Bankkonto, die die Attribute

* `_kontoinhaber` und
* `_kontostand`

und die Methoden

* `einzahlen(self, betrag)`
* `abheben(self, betrag)` und
* `__str__(self)`

hat.

Der `_kontostand` soll im Konstruktor `__init__(...)` initial auf 0 gesetzt werden. Der Kontoinhaber soll an den Konstruktor übergeben werden: 
```python
...
    def __init__(self, kontoinhaber):
        self._kontoinhaber = kontoinhaber
        ...
```

Die Methode `einzahlen(betrag)` soll den Kontostand um den übergebenen Betrag erhöhen und den neuen Kontostand ausgeben.

Die Methode `abheben(betrag)` den soll den Kontostand um den angegebenen Betrag verringern, sofern der Kontostand dafür ausreichend ist. Ansonsten soll das Abheben mit einer Fehlerausgabe abgebrochen werden.

Die Methode `__str__()` soll ebenfalls definiert werden und soll einen String zurückgeben, der den Inhaber und den Kontostand wiedergibt, z.B. 'Inhaber: ..., Kontostand: ...'. Diese Methode wird z.B. automatisch aufgerufen, wenn man `print(konto)` aufruft (`konto` soll ein Objekt der Klasse Bankkonto).

Anschließend sollen folgende Anweisungen ausgeführt werden:

```python
konto1 = Bankkonto("Alice")
print(konto1)
konto1.einzahlen(100)
print(konto1)
konto1.abheben(30)
print(konto1)
konto1.abheben(200) # sollte Fehler ausgeben
```