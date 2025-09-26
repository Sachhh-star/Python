import random
teller = 0
worp = 0
while(worp < 12):
    dobbelst1 = random.randint(1,6)
    dobbelst2 = random.randint(1,6)
    worp = dobbelst1 + dobbelst2 
    worp = random.randint(2,12)
    teller += 1
print(str(worp) + " pogin " + str(teller))
print(f"{worp} poging {teller}")

