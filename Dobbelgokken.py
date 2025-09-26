import random
#er een random getal komen tussen 1 en 6: dit getal zet ik in worp
worp = random.randint(1,6)
#de grbruiker moet een gok in kunnen voeren
#het ingevoerder getal door de grbruiker moet opgepakt worden: dit getal zet ik in gok
gok = int(input("Gok het getal"))
#worp en gok moeten met elkaar vergegeleken worden: als gok: worp dan 'hoera', anders 'duipje omlaag
if (worp == gok):
    print("Goed")
else:
    print("fout gegokt!")
