nb_heros_per_round = [O] * nbRound
total_pull_heros = 0
nb_total_heros = 116
#37force
#37agi
#42intel
while True:
    if nb_players <= 0 or nb_players > 5 :
        break
    else :
        continue

nb_round = int(input("How many rounds to win ?"))
nb_heros_per_round = [O] * nbRound
total_pull = 0
nb_total_heros = 116

for round in nbRound :
  nb_heros_per_round[round] = int(input("How many heros per round (1-20)?"))
  if nb_heros_per_round[round] < 1 or nb_heros_per_round[round] > 20 :
    break
  else :
    continue
    total_pull = nb_players * nb_heros_per_round + total_pull
    if totalpull > nb_total_heros :
        print("Too much heros in rounds")
        break
    else :
        continue
