print("Kies dit 1-6 opties!")
print("1. Hoeveel is x% van y?")
print("2. x is y% van z - wat is z?")
print("3. Een getal stijgt met X%")
print("4. Een getal daalt met X%")
print("5. Wat is een nieuwe % stijging van x?")
print("6. What is een nieuwe % daling van x?")

Opties = int(input("Voer je opties in (1-6):"))
match Opties:
    case 1:
        x = float(input("Voer het percentage (x): "))
        y = float(input("Voer het getel (y): "))
        antwoord = (x / 100) * y
        print(f"\n{x}% van {y} = {antwoord}")
        print(f"Berekening: {x}/100 × {y} = {antwoord}")
    case 2:
            x = float(input("Voer het bedrag (X): "))
            y = float(input("Voer het percentage (Y%): "))
            antwoord = x / (y / 100)
            print(f"\n{x} is {y}% van {antwoord}")
            print(f"Berekening: {x} ÷ ({y}/100) = {antwoord}")
    case 3:
            oud = float(input("Voer de oude waarde in: "))
            x = float(input("Percentage toename: "))
            antwoord = oud * (1 + x / 100)
            print(f"\nNieuwe waarde = {oud} × (1 + {x}/100) = {antwoord}")
    case 4:
            oud = float(input("Voer de oude waarde in: "))
            x = float(input("Percentage afname: "))
            antwoord = oud * (1 - x / 100)
            print(f"\nNieuwe waarde = {oud} × (1 - {x}/100) = {antwoord}")
    case 5:
            oud = float(input("Oude waarde: "))
            nieuw = float(input("Nieuwe waarde: "))
            antwoord = ((nieuw - oud) / oud) * 100
            print(f"\nToename = (({nieuw} - {oud}) / {oud}) × 100 = {antwoord}%")

    case 6:
            oud = float(input("Oude waarde: "))
            nieuw = float(input("Nieuwe waarde: "))
            antwoord = ((oud - nieuw) / oud) * 100
            print(f"\nAfname = (({oud} - {nieuw}) / {oud}) × 100 = {antwoord}%")
    case _:
            print("Ongeldige keuze. Probeer opnieuw.")        
