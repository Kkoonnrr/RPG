import pandas as pd
import random
import objects
start = -1
stop = -1
name_found = False
weapon = pd.read_csv("RPG.csv", delimiter=";", keep_default_na=False)
weapons_generated = pd.DataFrame(weapon[weapon["Typ broni"].astype(bool)]["Typ broni"])
weapons_generated.index = ([x for x in range(1, 21)])
temp = weapon["Typ broni"][0]
for i, j in enumerate(weapon["Typ broni"]):
    if j == '':
        weapon["Typ broni"][i] = temp
    else:
        temp = j
chances1 = weapon[weapon["Nazwa"].astype(bool)]["Nazwa"]
chances2 = weapon[weapon["ilośc losowań"].astype(bool)]["ilośc losowań"]
chances = pd.DataFrame([chances1, chances2]).transpose().set_index("Nazwa")
place = "miasto"
num_of_items = int(chances["ilośc losowań"][place][0:2])
items = list()
for i in range(1, num_of_items+1):
    name_found = False
    modifier_found = False
    items.append(objects.Weapon(weapons_generated["Typ broni"][random.randrange(1, 3)]))
    j = 0
    item_iterator = 0
    for r in weapon["Typ broni"]:
        if r == items[-1].weapon_type and start == -1:
            start = item_iterator
        if r == items[-1].weapon_type and weapon["Typ broni"][item_iterator+1] != items[-1].weapon_type and stop == -1:
            stop = item_iterator
        item_iterator = item_iterator + 1
        if start >= 0 and stop >= 0:
            break
    name_chance = sum([float(weapon[place][o].replace(',', '.')) for o in range(start, stop + 1)]) * 100
    modifier_chance = sum([float(weapon["Szansa"][o].replace(',', '.')) for o in range(start, stop + 1)]) * 100
    j = start
    while not name_found:
        rand = random.randrange(1, int(name_chance))
        if rand <= float(weapon[place][j].replace(',', '.'))*100:
            items[-1].name = weapon["nazwa"][j]
            items[-1].accuracy = weapon["Celność"][j]
            items[-1].damage = weapon["Obrażenia"][j]
            items[-1].penetration = weapon["PP"][j]
            items[-1].weapon_range = weapon["Zasięg"][j]
            items[-1].strength_needed = weapon["Wymagana siła"][j]
            name_found = True
        j = j+1
        if j == stop+1:
            j = start
    j = start
    for i in range(0, 3):
        rand = random.randrange(1, int(name_chance))
        if rand <= float(weapon["Szansa"][j].replace(',', '.'))*100:
            items[-1].modifier.append(weapon["Modyfikator"][j])
        j = j + 1
        if j == stop + 1:
            j = start
    start = -1
    stop = -1
...
