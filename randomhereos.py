import json
from random import *

json_data = open("hero_modified.json").read()
data = json.loads(json_data)

json_param = open("players_rounds_tab.json").read()
param = json.loads(json_param)

list_of_id_str = []
list_of_id_agi = []
list_of_id_int = []

for hero in data:
	if hero["primary_attr"] == "str":
		list_of_id_str.append(hero["id"])
	elif hero["primary_attr"] == "agi":
		list_of_id_agi.append(hero["id"])
	if hero["primary_attr"] == "int":
		list_of_id_int.append(hero["id"])


print(list_of_id_str)
print(list_of_id_agi)
print(list_of_id_int)

print(len(list_of_id_agi))
print(len(list_of_id_str))
print(len(list_of_id_int))


print(param[2]["4rounds"])

for round in range (nb_round) :
    for hereos in nb_hereos_per_round
