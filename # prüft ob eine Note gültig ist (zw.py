# prüft ob eine Note gültig ist (zw. 1 und 6)
# gibt in dem fall True zurück, ansonsten (0, -10, "foo") False
def ist_gueltige_note(note: int) -> bool:
    pass

# berechnet den Durchschnitt einer Liste von Noten
# wirft ValueError wenn die Liste leer ist
# wirft Value Error wenn eine Note für ist_gueltige_note() false zurückgibt
def durchschnitt(noten: list[int]) -> float:
    pass

# gibt die beste Note zurück
# wirft ValueError wenn die Liste leer ist
def beste_note(noten: list[int]) -> int:
    pass


# wandelt Note in Text um (1 -> "sehr gut" usw)
# wirft ValueError wenn ist_gueltige_note() false zurückgibt
def note_zu_text(note: int) -> str:
    pass