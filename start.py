MIN_NB_PLAYER = 1
MAX_NB_PLAYER = 5
NB_HEROES = 116
ERROR_NB_PLAYER_INPUT = "La valeur entrée n'est pas un entier compris entre {} et {}\n".format(MIN_NB_PLAYER, MAX_NB_PLAYER)


success = False
nb_joueur = 0

while not success:
    try:
        nb_joueur = int(input("Entrer le nombre de joueur (entre {} et {}):\n".format(MIN_NB_PLAYER, MAX_NB_PLAYER)))
        if (nb_joueur <= MAX_NB_PLAYER) and (nb_joueur >= MIN_NB_PLAYER):
            success = True
        else:
            print(ERROR_NB_PLAYER_INPUT)
    except ValueError:
        print(ERROR_NB_PLAYER_INPUT)

print("Vous avez sélectionné {} joueur(s)!".format(nb_joueur))
