import json

json_data = open("hero_modified.json").read()
data = json.loads(json_data)

hero_list_id = [0] * 116
for hero in data:
    hero_list_id[hero] = 'id'

for hero in range (116) :
    print(hero_list_id[hero])
