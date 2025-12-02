Aufgabe 1

Zeichne ein Klassendiagramm, welches die Klassen Animal, Dog und Cat aus dem animal.py Beispiel enthält und ihre Beziehung darstellt.
Aufgabe 2

Zeichne ein Sequenzdiagramm für bankkonto_mit_bank.py, so wie wie sequenzdiagramm1.png, aber mit der Änderung, dass die abheben() Methode True oder False zurückgibt, je nachdem ob das Abheben erfolgreich war, und die Überweisung (also das Anschließende Einzahlen) nur bei erfolgreichem Abheben durchgeführt wird.
Aufgabe 3

In einer Banksoftware sollen zwei verschiedene Kontotypen mittels Klassen abgebildet werden. Alle Bankkonten haben die Methode Attribute Kontonummer und Kontostand und die Methoden einzahlen(betrag), auszahlen(betrag) und eine Methode info(), welche Informationen zum Konto ausgibt.
Sparkonto

    hat einen Zinssatz, dieser wird mit zinsen_gutschreiben() auf das Guthaben angewendet und der Kontostand entsprechend erhöht
    abheben(betrag) darf nur erfolgreich sein, wenn der Kontostand dafür ausreicht, er darf also nicht negativ werden

Girokonto

    hat einen Überziehungsrahmen
    abheben(betrag) darf nur innerhalb des Überziehungsrahmens erfolgreich sein, der Kontostand darf also höchstens bis zum Überziehungsrahmen negativ sein, wenn also z.B. Überziehungsrahmen 1000 € ist, dann darf der Kontostand -1000 € sein, aber nicht niedriger

Schreib im Anschluss ein Programm um diese zwei Kontoarten als Objekte anzulegen und deren Methoden zu testen.