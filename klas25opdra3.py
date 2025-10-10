import random

naam = ["Daan A.", "Abdul","Yaroslav", "Beam","Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V", "Kateryna"]
x = int(input("Kies de nummers dat je wil."))
gekozen = random.sample(naam, x)
print("Gekozen naam", gekozen)