## unittest assert-Cheatsheet — Druckversion (A4, einseitig)

Hinweis: kurze Beispiele zeigen typische Nutzung; ersetze obj/werte nach Bedarf.

----------------------------------------------------------------------

Allgemeines
- Verwendung in TestCase-Methoden: self.assertX(actual, expected[, msg]) oder self.assertX(a, b, ...)
- Viele Methoden akzeptieren optional msg.

----------------------------------------------------------------------

Grundlegende Vergleiche

| Methode | Bedeutung | Signatur | Beispiel |
|---|---:|---|---|
| **assertEqual** | Gleichheit (==) | self.assertEqual(a, b, msg=None) | self.assertEqual(result, 42) |
| **assertNotEqual** | Ungleichheit (!=) | self.assertNotEqual(a, b) | self.assertNotEqual(value, 0) |
| **assertTrue** | Wahr | self.assertTrue(x) | self.assertTrue(flag) |
| **assertFalse** | Falsch | self.assertFalse(x) | self.assertFalse(is_empty) |
| **assertIs** | Identität (is) | self.assertIs(a, b) | self.assertIs(obj, None) |
| **assertIsNot** | Nicht-identisch | self.assertIsNot(a, b) | self.assertIsNot(a, b) |
| **assertIsNone** | Ist None | self.assertIsNone(x) | self.assertIsNone(maybe) |
| **assertIsNotNone** | Nicht None | self.assertIsNotNone(x) | self.assertIsNotNone(value) |

----------------------------------------------------------------------

Vergleiche mit Ordnung (Zahlen)

| Methode | Bedeutung | Beispiel |
|---|---:|---|
| **assertGreater** | a > b | self.assertGreater(a, b) |
| **assertGreaterEqual** | a >= b | self.assertGreaterEqual(a, b) |
| **assertLess** | a < b | self.assertLess(a, b) |
| **assertLessEqual** | a <= b | self.assertLessEqual(a, b) |

----------------------------------------------------------------------

Näherungs-/Float-Vergleich

| Methode | Bedeutung | Signatur | Beispiel |
|---|---:|---|---|
| **assertAlmostEqual** | rund bis places oder delta | self.assertAlmostEqual(a, b, places=7, delta=None) | self.assertAlmostEqual(0.1+0.2, 0.3, places=7) |
| **assertNotAlmostEqual** | nicht nahe | self.assertNotAlmostEqual(a, b, places=7) | |

----------------------------------------------------------------------

Sequenzen, Sets, Dictionaries

| Methode | Bedeutung | Beispiel |
|---|---:|---|
| **assertIn** | Mitgliedschaft | self.assertIn(member, container) |
| **assertNotIn** | Nicht-Mitglied | self.assertNotIn(member, container) |
| **assertSequenceEqual** | Sequenz-Genauvergleich | self.assertSequenceEqual(seq1, seq2) |
| **assertListEqual** | List-Vergleich | self.assertListEqual(list1, list2) |
| **assertTupleEqual** | Tuple-Vergleich | self.assertTupleEqual(t1, t2) |
| **assertSetEqual** | Set-Vergleich | self.assertSetEqual(s1, s2) |
| **assertDictEqual** | Dict-Vergleich | self.assertDictEqual(d1, d2) |

----------------------------------------------------------------------

Typ-Checks

| Methode | Bedeutung | Beispiel |
|---|---:|---|
| **assertIsInstance** | isinstance(obj, cls) | self.assertIsInstance(obj, MyClass) |
| **assertNotIsInstance** | nicht Instanz | self.assertNotIsInstance(obj, OtherClass) |

----------------------------------------------------------------------

Ausnahmen & Warnungen

| Konstruktion | Bedeutung | Beispiel |
|---|---:|---|
| **assertRaises (context manager)** | erwartet Exception | with self.assertRaises(ValueError): func(bad) |
| **assertRaisesRegex** | Exception + Regex-Match | with self.assertRaisesRegex(ValueError, "invalid"): f(bad) |
| **assertWarns** | erwartet Warnung | with self.assertWarns(UserWarning): warnfunc() |
| **assertLogs** | prüft Logging-Ausgaben | with self.assertLogs('mod', level='INFO') as cm: f() |

----------------------------------------------------------------------

Hilfs-/Sonstiges

| Methode | Bedeutung | Beispiel |
|---|---:|---|
| **fail** | Test sofort fehlschlagen | self.fail("unreachable") |
| **skipTest** | Test überspringen | self.skipTest("reason") |
| **subTest** | Untertests/Parametrisierung | for x in vals: with self.subTest(x=x): self.assertTrue(f(x)) |

----------------------------------------------------------------------

Kurzreferenz — typische Signaturen
- self.assertEqual(a, b[, msg])
- self.assertTrue(x[, msg])
- with self.assertRaises(ExceptionType): ...
- self.assertAlmostEqual(a, b[, places=7[, delta=None]])

----------------------------------------------------------------------

Druckhinweise
- Seitenränder schmal (10–12 mm) für A4 einseitig.
- Schriftgröße 10–11 pt, monospace für Codebeispiele.
- Empfohlen: zweimal gefaltetes A4 (Z-Falz) oder Laminat für Handhabung.

----------------------------------------------------------------------

Datei zum Drucken
- Um aus Markdown eine PDF zu erzeugen, verwende z. B.:
  pandoc cheatsheet.md -o cheatsheet.pdf --pdf-engine=xelatex -V geometry:margin=10mm -V fontsize=10pt

(Ende)
