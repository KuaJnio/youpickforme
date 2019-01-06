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
ERROR_ANSWER_AUTO_ROUND = "Votre réponse ne correpond pas à 'yes' ou 'no'."

import json
from random import *

json_data = open("hero_modified.json").read()
data = json.loads(json_data)

list_of_id = []
list_of_id_str = []
list_of_id_agi = []
list_of_id_int = []

liste2joueurs = [ [35, 23], [25, 18, 15], [20, 17, 15, 6], [20, 16, 11, 8, 3], [18, 15, 12, 8, 4, 1], [18, 15, 10, 8, 4, 2, 1], [15, 12, 10, 8, 6, 4, 2, 1], [12, 11, 10, 8, 6, 5, 3, 2, 1], [12, 10, 8, 7, 6, 5, 4, 3, 2, 1] ]
liste3joueurs = [ [23, 13], [20, 14, 4], [20, 10, 5, 3], [16, 11, 7, 3, 1], [14, 10, 7, 4, 2, 1], [11, 8, 7, 5, 4, 2, 1], [9, 8, 6, 5, 4, 3, 2, 1], [8, 7, 6, 5, 4, 3, 2, 2, 1], [7, 6, 5, 5, 4, 3, 3, 2, 2, 1] ]
liste4joueurs = [ [18, 11], [16, 10, 3], [14, 9, 4, 2], [12, 8, 5, 3, 1], [10, 8, 5, 3, 2, 1], [8, 6, 5, 4, 3, 2, 1], [6, 6, 5, 4, 3, 2, 2, 1], [6, 5, 4, 3, 3, 3, 2, 2, 1], [5, 4, 4, 4, 3, 3, 2, 2, 1, 1] ]
liste5joueurs = [ [18, 11], [16, 10, 3], [14, 9, 4, 2], [12, 8, 5, 3, 1], [10, 8, 5, 3, 2, 1], [8, 6, 5, 4, 3, 2, 1], [6, 6, 5, 4, 3, 2, 2, 1], [6, 5, 4, 3, 3, 3, 2, 2, 1], [5, 4, 4, 4, 3, 3, 2, 2, 1, 1] ]

nb_hereos_per_round = [0]
nb_hereos_remaining = NB_HEROES
nb_hereos_remaining_player = 0

for hero in data:
	if hero["primary_attr"] == "str":
		list_of_id_str.append(hero["id"])
	elif hero["primary_attr"] == "agi":
		list_of_id_agi.append(hero["id"])
	elif hero["primary_attr"] == "int":
		list_of_id_int.append(hero["id"])

for hero in data:
    list_of_id.append(hero["id"])

success = False
nb_joueur = 0
print("You Pick for Me - v. alpha - aut0wash & KuaJ")
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

listJ1 = nb_hereos_per_round
listJ2 = nb_hereos_per_round
if nb_joueur >= 3:
    listJ3 = nb_hereos_per_round
if nb_joueur >= 4:
    listJ4 = nb_hereos_per_round
if nb_joueur >= 5:
    listJ5 = nb_hereos_per_round

az = 4
name_joueur = ['J1', 'J2', 'J3', 'J4', 'J5']
if nb_joueur < 5:
    for loop in range (5-nb_joueur):
        del name_joueur[az]
        az = az-1


success = False
answer_name_player = None
while not success:
    try:
        answer_name_player = None
        answer_name_player = str.upper(input("Voulez-vous rentrer les pseudos des joueurs (par défaut : Joueur 1) : 'yes' or 'no'\n"))
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

print("Les joueurs sont :", end=" ")
for joueur in range (nb_joueur):
    print(name_joueur[joueur], end=", ")
print(" ")


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


success = False
answer_auto_round = None
while not success:
    try:
        answer_auto_round = None
        answer_auto_round = str.upper(input("Souhaitez-vous utiliser les paramètres par défaut pour chaque round ? 'yes' ou 'no'\n" ))
        if answer_auto_round == 'YES':
            if nb_joueur == 2:
                nb_hereos_per_round = liste2joueurs[nb_round-2]
            if nb_joueur == 3:
                nb_hereos_per_round = liste3joueurs[nb_round-2]
            if nb_joueur == 4:
                nb_hereos_per_round = liste4joueurs[nb_round-2]
            if nb_joueur == 5:
                nb_hereos_per_round = liste5joueurs[nb_round-2]
            success = True
        elif answer_auto_round == 'NO':
            print("Les valeurs par défaut ne seront pas utilisées")
            success = True
        elif (answer_auto_round != 'YES') or (answer_auto_round != 'NO'):
            print(ERROR_ANSWER_AUTO_ROUND)
    except ValueError:
        print(ERROR_ANSWER_AUTO_ROUND)



def ask_input(round):
    erreur = False
    while not erreur:
        nb_hereos_per_round[round] = int(input("Entrer le nombre de héros par joueur pour le round n°{}/{} (entre {} et {}):\n".format(round+1, nb_round, MIN_NB_HEREOS_PER_ROUND, MAX_NB_HEREOS_PER_ROUND)))
        if nb_hereos_remaining >= 0 :
            return nb_hereos_per_round[round]
            erreur = True
        else :
            return None

if answer_auto_round == 'NO':
    success = False
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
nb_hereos_remaining = NB_HEROES - pull_hereos


list_general = []
rang = 0
compteur = 0
for round in range (nb_round):
    print("Round {} sur {} :\n".format(round+1, nb_round))
    success = False
    for i in range (nb_joueur):
        pick_list = [0] * nb_hereos_per_round[round]
        for hereos in range (nb_hereos_per_round[round]):
            pick_list[hereos] = choice(list_of_id)
            b = list_of_id.index(pick_list[hereos])
            del list_of_id[b]
        name_list = []
        for hero in data:
            if hero["id"] in pick_list:
                name_list.append(hero["localized_name"])
        print(name_joueur[i])
        print(name_list)
        print(" ")
        list_general.append(name_list)
    while not success:
        answer_result = str.upper(input("Victory ? : 'yes' or 'no'\n"))
        if answer_result == 'YES':
            print(" ")
            compteur = compteur +1
            round = round +1
            success = True
        if answer_result == 'NO':
            print(" ")
            print("Round {} sur {} :\n".format(round+1, nb_round))
            compteur = compteur + 1
            rang = round * nb_joueur
            for joueur in range (nb_joueur):
                print(name_joueur[joueur])
                print(list_general[rang + joueur])
                print(" ")

print("Victoire de la totalité des {} manches, en {} parties jouées !\n".format(nb_round, compteur))
input()
