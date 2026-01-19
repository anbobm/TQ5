from unittest import TestCase

from notenverwaltung import ist_gueltige_note, durchschnitt, beste_note, note_zu_text


class TestIstGueltigeNote(TestCase):

    # 1 test für gültige Noten (1, 3, 6)
    # 1 test für ungültige Noten (0, 7, -1)
    # 1 test für ungültige Typen (2.5, "2", None)
    pass


class TestDurchschnitt(TestCase):

    # 1 test für durchschnitt mehrerer noten z.B. [2, 3, 4]
    # 1 test für durchschnitt einzelner note z.B. [1]
    # 1 test für Leere Liste []
    # 1 test für ungültige Note in Liste z.B. [2, 3, 7]
    pass

class TestBesteNote(TestCase):

    # 1 test für beste Note z.B. [2, 3, 5]
    # 1 test für beste Note in unsortierter Liste z.B. [6, 1, 4, 2]
    # 1 test für leere Liste []
    pass


class TestNoteZuText(TestCase):

    # 1 test für alle Noten 1 -> "sehr gut", usw
    # 1 test für ungültige Noten, z.B. 0, 7
    pass