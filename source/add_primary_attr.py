import json
from collections import OrderedDict

jsonFile = open("heroes.json", "r")
heroes = json.load(jsonFile, object_pairs_hook=OrderedDict)
jsonFile.close()

json_data2 = open("heroes_opendota.json").read()
data2 = json.loads(json_data2)


for hero in heroes:
    for it in data2:
        if hero['id'] == it['id']:
            hero['primary_attr'] = it['primary_attr']
    hero.pop('url_full_portrait', None)
    hero.pop('url_small_portrait', None)
    hero.pop('url_large_portrait', None)
    hero.pop('url_vertical_portrait', None)

jsonFile = open("hero_modified.json", "wb+")
jsonFile.write(json.dumps(heroes, ensure_ascii=False, indent=4, sort_keys=False).encode('utf8'))
jsonFile.close()
