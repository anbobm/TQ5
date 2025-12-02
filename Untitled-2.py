while True:
    print("[1] ...")
    print("[2] ...")
    eingabe = input("Welches ..? ")
    try:
        nummer = int(eingabe)
        break
    except ValueError:
        print("Ungültige Eingabe")

if nummer == 1:
    pass
elif nummer == 2:
    pass