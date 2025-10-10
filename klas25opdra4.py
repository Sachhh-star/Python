import random

naam = ["Daan A.", "Abdul","Yaroslav", "Beam","Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V", "Kateryna"]

x = int(input("persoon in een groupje:"))
y = int(input("aantal groupje:"))
if x * y > len(naam):
    print("Niet genoeg namen")
else:
    random.shuffle(naam)
    for i in range(y):
        print(f"Groep {i+1}:", naam[i*x:(i+1)*x])