#### Aufgabe

Erweitere die `bibo_lösung.py` um eine Import-Funktionalität. Dabei sollen aus einer Datei, in der Bücher in folgendem Format (Titel, Erscheinungsjahr, Autor, Seitenzahl) gespeichert werden, Bücher-Objekte erzeugt und dem Bibliothek-Objekt hinzugefügt werden:

```
Das Boot,1973,Lothar-Günther Buchheim,603
Harry Potter and the Philosopher's Stone,1997,J.K. Rowling,223
```

Einlesen einer (utf-8-kodierten) Datei in einen String:
```python
with open("datei.txt", encoding="utf-8") as file:
    komplettstring = file.read()
```

Einen String anhand eines Trenners splitten:
```python
s = "abc-def-012"
liste = s.split("-") # ['abc', 'def', '012']
```

Einen String der mehrere Zeilen enthält in einzelne Zeilen splitten:
```python
s = "abc\ndef\n"
zeilen = s.splitlines() # ['abc', 'def']
```