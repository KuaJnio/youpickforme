from math import *
MIN_NB_PLAYER = 1
MAX_NB_PLAYER = 5
MIN_NB_ROUND = 1
MAX_NB_ROUND = 10
MIN_NB_HEREOS_PER_ROUND = 1
MAX_NB_HEREOS_PER_ROUND = 20

NB_HEROES = 116

ERROR_NB_PLAYER_INPUT = "La valeur entrée n'est pas un entier compris entre {} et {}\n".format(MIN_NB_PLAYER, MAX_NB_PLAYER)
ERROR_NB_ROUND_INPUT = "La valeur entrée n'est pas un entier compris entre {} et {}\n".format(MIN_NB_ROUND, MAX_NB_ROUND)
ERROR_NB_HEREOS_PER_ROUND_INPUT = "La valeur entrée n'est pas un entier compris entre {} et {}\n".format(MIN_NB_HEREOS_PER_ROUND, MAX_NB_HEREOS_PER_ROUND)
ERROR_TOO_MUCH_HEREOS = "Il n'y a pas suffisamment de héros disponibles pour permettre cette répartition \nVeuillez sélectionner moins de héros\n"
ERROR_ANSWER_REDISTRIBUTION_REMAINING = "Votre réponse ne correspond pas à 'yes' ou 'no'."
ERROR_ANSWER_NAME_JOUEUR = "Votre réponse ne correspond pas à 'yes' ou 'no'."

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
	elif hero["primary_attr"] == "int":
		list_of_id_int.append(hero["id"])

success = False
nb_joueur = 0

while not success:
    try:
        nb_joueur = int(input("Entrer le nombre de joueur (entre {} et {}) :\n".format(MIN_NB_PLAYER, MAX_NB_PLAYER)))
        if (nb_joueur <= MAX_NB_PLAYER) and (nb_joueur >= MIN_NB_PLAYER):
            success = True
        else:
            print(ERROR_NB_PLAYER_INPUT)
    except ValueError:
        print(ERROR_NB_PLAYER_INPUT)

print("Vous avez sélectionné {} joueur(s)!".format(nb_joueur))


success = False
nb_round = 0
while not success:
    try:
        nb_round = int(input("Entrer le nombre de rounds pour gagner (entre {} et {}) :\n".format(MIN_NB_ROUND, MAX_NB_ROUND)))
        if (nb_round <= MAX_NB_ROUND) and (nb_round >= MIN_NB_ROUND):
            success = True
        else :
            print(ERROR_NB_ROUND_INPUT)
    except ValueError:
            print(ERROR_NB_ROUND_INPUT)
print("Vous avez choisi {} round(s) pour gagner !".format(nb_round))

def ask_input(round):
    erreur = False
    while not erreur:
        nb_hereos_per_round[round] = int(input("Entrer le nombre de héros par joueur pour le round n°{}/{} (entre {} et {}):\n".format(round+1, nb_round, MIN_NB_HEREOS_PER_ROUND, MAX_NB_HEREOS_PER_ROUND)))
        if nb_hereos_remaining >= 0 :
            return nb_hereos_per_round[round]
            erreur = True
        else :
            return None

success = False
nb_hereos_per_round = [0]
nb_hereos_remaining = 0
nb_hereos_remaining_player = 0
while not success:
    try:
        nb_hereos_per_round = [0] * nb_round
        nb_hereos_remaining = NB_HEROES
        nb_hereos_remaining_player = nb_hereos_remaining/nb_joueur
        for round in range (nb_round):
            print("{}/{} sont disponibles soit {} héros disponibles par joueur\n".format(nb_hereos_remaining, NB_HEROES, floor(nb_hereos_remaining_player)), end ='')
            if nb_hereos_remaining%nb_joueur >0 :
                print("et {} héros restant non distribuable(s) équitablement\n".format(nb_hereos_remaining%nb_joueur))
            ask_input(round)
            if (nb_hereos_per_round[round] <= MAX_NB_HEREOS_PER_ROUND) and (nb_hereos_per_round[round] >= MIN_NB_HEREOS_PER_ROUND):
                nb_hereos_remaining = nb_hereos_remaining - (nb_joueur * nb_hereos_per_round[round])
                nb_hereos_remaining_player = nb_hereos_remaining/nb_joueur
            else :
                print(ERROR_NB_HEREOS_PER_ROUND_INPUT)
            if nb_hereos_remaining < 0:
            	break
        if nb_hereos_remaining >= 0 :
            success = True
        else:
            print(ERROR_TOO_MUCH_HEREOS)
            success = False
    except ValueError:
            print(ERROR_NB_HEREOS_PER_ROUND_INPUT)

print("Vous avez choisi", nb_hereos_per_round, "pour chaque round !")

pull_hereos = 0

for round in range (nb_round) :
    pull_hereos = nb_joueur * nb_hereos_per_round[round] + pull_hereos
print("{} parmi les {} héros seront proposés, {} héros non distribué(s) !\n".format(pull_hereos, NB_HEROES, NB_HEROES-pull_hereos))

if nb_hereos_remaining > 0:
    success = False
    answer_redistribution_remaining = None
    while not success:
        try:
            answer_redistribution_remaining = None
            answer_redistribution_remaining = str.upper(input("Voulez-vous redistribuer aléatoirement les héros restant à certains joueurs : 'yes' or 'no'"))
            if answer_redistribution_remaining == 'YES':
                print("{} héros redistribué(s) aléatoirement au premier round\n".format(NB_HEROES-pull_hereos))
                success = True
            elif answer_redistribution_remaining == 'NO':
                print("{} héros absent(s) du jeu\n".format(NB_HEROES-pull_hereos))
                success = True
            elif (answer_redistribution_remaining != 'YES') or (answer_redistribution_remaining != 'NO'):
                print(ERROR_ANSWER_REDISTRIBUTION_REMAINING)
        except ValueError:
            print(ERROR_ANSWER_REDISTRIBUTION_REMAINING)


name_joueur = [0] * nb_joueur

success = False
answer_name_player = None
while not success:
    try:
        answer_name_player = None
        answer_name_player = str.upper(input("Voulez-vous rentrer les pseudos des joueurs (par défaut : Joueur 1) : 'yes' or 'no'"))
        if answer_name_player == 'YES':
            for joueur in range (nb_joueur):
                name_joueur[joueur] = input("Pseudo du joueur {}/{} :\n".format(joueur+1, nb_joueur))
            success = True
        elif answer_name_player == 'NO':
            print("Pseudo(s) par défaut utilisé(s)")
            success = True
        elif (answer_name_player != 'YES') or (answer_name_player != 'NO'):
            print(ERROR_ANSWER_NAME_JOUEUR)
    except ValueError:
        print(ERROR_ANSWER_NAME_JOUEUR)

print(name_joueur)
round = 0
for round in range (0, nb_round, 1):
    pick_list = [0] * nb_hereos_per_round[round]
    for hereos in range (nb_hereos_per_round[round]):
        pick_list[hereos] = choice(list_of_id_agi)
        b = list_of_id_agi.index(pick_list[hereos])
        del list_of_id_agi[b]
    name_list = []
    round = round +1
    for hero in data:
        if hero["id"] in pick_list:
            name_list.append(hero["localized_name"])
    print(name_list)
