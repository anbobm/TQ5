# TQ5 Repository

Hier könnt ihr euch mit git und GitHub ausprobieren.

Nachfolgend eine Zusammenfassung: Alles was wir uns angeschaut haben, aber nicht alles mit gleicher Gründlichkeit. Zum Teil wurden Dinge auch nur kurz erwähnt. Manchmal zähle ich es nur auf, manchmal wiederhole ich es auch ein bisschen.

## Python

### Syntax

* Leerzeichen bzw. 'Whitespace' ist bedeutungslos außer:
  * am Zeilenanfang, dort stellen sie eine Einrückung (Indentation) dar und kennzeichnen, welche Abschnitte von Instruktionen zu einem Block gehören. z.B.:
```python
if ausdruck:
    i += 1          # eingerückt, gehört zum if-Block
    print('foo')    # eingerückt, gehört zum if-Block
print('bar')        # nicht eingerückt, gehört nicht mehr zum if-Block
```
  * in Strings:
  ```python
    'Hallo Paul' != 'Hallo     Paul'
  ```
### Kontrollstrukturen

* Verzweigungen mit `if`, `elif` und `else`
* `match ... case` (nur erwähnt)
* Schleifen mit `for ... in ...`
* Schleifen mit `while`

### Datentypen

* Strings, Ganzzahlen, Fließkommazahlen
* Strings interpolieren mit f-Strings: `f'Hallo {name}'`
* Listen: `liste = [1, 2, 3, 'apfel']`, leere Liste: `[]`
* erwähnt: slices `liste[2:6]` gibt `liste` zurück, aber nur von Index 2 bis (exklusive) 6, also Indexe 2, 3, 4 und 5
* `range(12,17)` gibt "Liste" zurück von 12 bis (exklusive) 25, also `[12, 13, 14, 15, 16]`
* Dictionaries `dict = { 'key' : value }`, leeres Dictionary: `{}`
* Datentypen umwandeln, z.B. String in Ganzahl: `int('3')`, nützlich um eine Zahl von der Konsole einzulesen

### Operatoren

* arithmetisch: `+`, `-`, `*`, `/`, `//`, `%`... z.B. `3 + 5`
* Vergleich: `>=` (größer gleich), `==` (gleich), `!=` (ungleich), etc... liefert Wahrheitswert (bool) zurück, ist also wahr (`True`) oder unwahr (`False`). Z.B. `3 == 5` ist `False`, `3 != 5` ist `True`, `3 < 5` ist `True`, usw.
* Zuweisung: `variable = 3`
* kombinierte Zuweisung: `variable += 3` (entspricht `variable = variable + 3`), `-=`, `*=`, ...

### Funktionen

* Programmcode den man an beliebigen Stellen Aufrufen kann
* definieren mit `def`, z.B.
```python
def hallo():
    ...
    ...
```
* Aufrufen mit `hallo()`
* Es kann Parameter geben, z.b. `print('Hallo!')`
* eingebaute Funktionen: `print()` zum Ausgeben, `input()` zum Einlesen

### I/O (Input/Output)

* Ausgeben ins Terminal: `print('Hello World')`
* Nutzereingaben vom Terminal einlesen: `eingabe = input()`

### Module

* importieren: `import math`
* modul verwenden: `print(math.pi)`
* gezielte Elemente importieren: `from math import pi` → `print(pi)`
* eigene Module schreiben: Datei `mymodule.py` schreiben, dann woanders importieren mit `import mymodule`