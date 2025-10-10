import random

naam = ["Daan A.", "Abdul","Yaroslav", "Beam","Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V", "Kateryna"]
nummer = random.choice(naam)
print(f"randon naam is {nummer}")
print(naam[random.randint(0, len(naam)-1)]) 