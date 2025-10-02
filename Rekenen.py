import random

def oefen_tafel():
    print("Welkom bij de tafeloefening!")
    tafel = int(input("Welke tafel wil je oefenen? Voer een getal in: "))

    score = 0
    for i in range(1, 11):  # 10 sommen
        factor = random.randint(1, 10)
        antwoord = int(input(f"Som {i}: {tafel} x {factor} = "))

        if antwoord == tafel * factor:
            print("Goed!")
            score += 1
        else:
            print(f"Fout! Het juiste antwoord is {tafel * factor}")

    print(f"\nJe bent klaar! Je score is {score} van de 10.")