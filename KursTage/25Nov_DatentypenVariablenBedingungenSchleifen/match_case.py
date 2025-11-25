fruit = input()

# fallunterscheidung mit match-case

match fruit:
    case "apple":
        print("Das war ein Apfel")
    case "banana":
        print("Das war eine Banane")
    case _: # default case wenn keiner der obigen fälle zutraf
        print("Das gibt's nicht")

# alternative mit if-elif-else

if fruit == "apple":
    print("Das war ein Apfel")
elif fruit == "banana":
    print("Das war eine Banane")
else:
    print("Das gibt's nicht")