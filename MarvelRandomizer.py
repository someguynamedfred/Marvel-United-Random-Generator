import random
herolist = []
with open ("MUH.txt") as myfile:
    for myline in myfile:
        herolist.append(myline.rstrip("\n"))
size = (len(herolist) - 1)
hero = random.randint(0,int(size))
loop = 1
herolist2 = []
while loop < 5:
    #print (herolist[hero])
    hero_to_list = (herolist[hero])
    herolist2.append(hero_to_list)
    herolist.pop(hero)
    #print (herolist)
    size = (size - 1)
    hero = random.randint(0,int(size))
    loop = (loop + 1)
print (herolist2)

villainlist = []

with open ("MUV.txt") as myfile:
    for myline in myfile:
        villainlist.append(myline.rstrip("\n"))

amount_villains = (len(villainlist) - 1)

villain = random.randint(0,int(amount_villains))

print (villainlist[villain])

villainlist.sort()
herolist.sort()

print (villainlist)
input (herolist)