import sys
import matplotlib.pyplot as plt
import matplotlib as mpl  # Zugriff auf moderne Farbkarten (Colormaps)
import numpy as np

# Import der PyQt6-Werkzeuge für das Fenster-Design
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
# Einbindung von Matplotlib-Grafiken in die PyQt-Oberfläche
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class FibonacciApp(QWidget):
    """
    Eine grafische Benutzeroberfläche (GUI) zur Visualisierung der Fibonacci-Folge.

    Diese Klasse erstellt ein Fenster mit PyQt6, berechnet die Zahlenfolge
    basierend auf Benutzereingaben und stellt die Ergebnisse in zwei
    dynamisch gefärbten, zoombaren Diagrammen dar.

    Attributes:
        figure (matplotlib.figure.Figure): Die Zeichenfläche für die Diagramme.
        canvas (FigureCanvas): Der Container, der die Grafik für PyQt anzeigt.
        toolbar (NavigationToolbar): Die interaktive Leiste zum Zoomen und Verschieben.
    """

    def __init__(self):
        """
        Initialisiert das Fenster und setzt Titel sowie die Standardgröße.
        """
        super().__init__()
        # Text in der Titelleiste des Fensters
        self.setWindowTitle("Fibonacci-Analyse: Interaktive Grafik")
        # Fenstergröße festlegen (x-Position, y-Position, Breite, Höhe)
        self.setGeometry(100, 100, 1000, 900) 

        # Ruft die Methode zum Erstellen der Knöpfe und Felder auf
        self.init_ui()

    def init_ui(self):
        """
        Erstellt die grafischen Elemente und ordnet sie in Layouts an.

        Dazu gehören das Eingabefeld, der Berechnungs-Button, das Textfeld
        für die Zahlen sowie die interaktive Grafikfläche mit Zoom-Leiste.
        """
        # Haupt-Layout: Ordnet alle Elemente von oben nach unten (vertikal) an
        main_layout = QVBoxLayout()

        # Horizontale Zeile für die Eingabe
        input_layout = QHBoxLayout()
        self.label_input = QLabel("Generationen (Monate):")
        self.entry_count = QLineEdit()
        self.entry_count.setPlaceholderText("z.B. 25")
        
        self.button_calculate = QPushButton("Berechnen & Visualisieren")
        # Wenn der Button geklickt wird, führe 'calculate_fibonacci' aus
        self.button_calculate.clicked.connect(self.calculate_fibonacci)

        # Elemente in die horizontale Zeile packen
        input_layout.addWidget(self.label_input)
        input_layout.addWidget(self.entry_count)
        input_layout.addWidget(self.button_calculate)
        
        # Die Zeile oben in das Hauptlayout einfügen
        main_layout.addLayout(input_layout)

        # Ein mehrzeiliges Feld zur Anzeige der berechneten Zahlen als Text
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True) # Nutzer kann hier nichts löschen
        self.text_output.setMaximumHeight(80)
        main_layout.addWidget(self.text_output)

        # --- Grafikbereich initialisieren ---
        # Eine weiße Zeichenfläche erstellen
        self.figure = Figure(figsize=(8, 10), facecolor='#ffffff')
        self.canvas = FigureCanvas(self.figure)
        
        # Die interaktive Leiste zum Zoomen über der Grafik platzieren
        self.toolbar = NavigationToolbar(self.canvas, self)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)

        # Das fertige Layout dem Fenster zuweisen
        self.setLayout(main_layout)

    def calculate_fibonacci(self):
        """
        Liest die Benutzereingabe aus und führt die mathematische Berechnung aus.

        Die Methode validiert die Eingabe, berechnet die Folge iterativ
        und stößt anschließend die grafische Darstellung an.

        Raises:
            ValueError: Wenn die Eingabe keine gültige ganze Zahl ist.
        """
        try:
            # Versuche, den Text im Eingabefeld in eine Zahl umzuwandeln
            input_text = self.entry_count.text()
            if not input_text: return
            
            count = int(input_text)
            # Logik-Check: Nur positive Zahlen machen Sinn
            if count <= 0:
                QMessageBox.warning(self, "Hinweis", "Zahl muss > 0 sein.")
                return

            # Die Fibonacci-Rechnung: Jede Zahl ist die Summe der zwei vorherigen
            folge = [0, 1]
            if count == 1:
                folge = [0]
            elif count > 2:
                for _ in range(2, count):
                    folge.append(folge[-1] + folge[-2])
            
            # Zahlen formatiert im Textfeld anzeigen
            self.text_output.setText(f"Folge: {' | '.join(map(str, folge))}")
            # Die Grafik-Funktion mit der berechneten Liste aufrufen
            self.plot_dynamic_colors(folge)

        except ValueError:
            # Fehlermeldung anzeigen, falls Text statt einer Zahl eingegeben wurde
            QMessageBox.critical(self, "Fehler", "Bitte eine Ganzzahl eingeben.")

    def plot_dynamic_colors(self, data):
        """
        Erstellt zwei Grafiken mit dynamischen Farbverläufen.

        Die Diagramme nutzen die 'plasma' Farbkarte, um steigende Werte
        farblich hervorzuheben. Die Darstellung erfolgt über Matplotlib.

        Args:
            data (list): Eine Liste der berechneten Fibonacci-Zahlen.
        """
        # Vorherige Grafik löschen, um Platz für die neue zu machen
        self.figure.clear()
        
        # Daten für Matplotlib vorbereiten (X-Achse = Index, Y-Achse = Wert)
        indices = np.array(range(len(data)))
        values = np.array(data)
        
        # Werte für die Farbauswahl normieren (Bereich 0.0 bis 1.0)
        v_min, v_max = values.min(), values.max()
        if v_min == v_max: v_max += 1 # Verhindert Fehler bei nur einer Zahl
        norm = mpl.colors.Normalize(v_min, v_max)
        
        # Die moderne Farbkarte 'plasma' laden (Lila -> Gelb)
        cmap = mpl.colormaps['plasma']

        # --- Oberer Plot: Die Kurve ---
        ax1 = self.figure.add_subplot(211) # 2 Reihen, 1 Spalte, 1. Bild
        ax1.plot(indices, values, color='#cccccc', zorder=1, alpha=0.5) # Graue Linie
        # Einzelne Punkte (Scatter) mit Farbwerten versehen
        ax1.scatter(indices, values, c=values, cmap=cmap, s=65, edgecolors='black', zorder=2)
        
        ax1.set_title("Wachstums-Tendenz (Farbverlauf)", fontweight='bold')
        ax1.set_ylabel("Zahlenwert")
        ax1.grid(True, linestyle=':', alpha=0.5)

        # --- Unterer Plot: Das Balkendiagramm ---
        ax2 = self.figure.add_subplot(212) # 2 Reihen, 1 Spalte, 2. Bild
        # Jedem Balken eine Farbe basierend auf seinem Wert zuweisen
        bar_colors = cmap(norm(values))
        bars = ax2.bar(indices, values, color=bar_colors, edgecolor='black', alpha=0.8)
        
        ax2.set_title("Population pro Generation", fontweight='bold')
        ax2.set_xlabel("Zeit (Generation n)")
        ax2.set_ylabel("Anzahl der Paare")

        # Beschriftung der Balken (nur wenn es nicht zu viele sind)
        if len(data) <= 25:
            for bar in bars:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height + (v_max * 0.01),
                         f'{int(height)}', ha='center', va='bottom', fontsize=8)

        # Layout-Anpassung, damit Titel und Beschriftungen nicht überlappen
        self.figure.tight_layout(pad=3.0)
        # Grafik auf dem Canvas neu zeichnen
        self.canvas.draw()

# Einstiegspunkt beim Start des Skripts
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Ein modernes Design für die Fenster-Elemente setzen
    app.setStyle("Fusion")
    
    # Das Fenster erstellen und anzeigen
    window = FibonacciApp()
    window.show()
    # Programm beenden, wenn das Fenster geschlossen wird
    sys.exit(app.exec())