# Задача 2. Случайные соревнования
import random
players_qty = 20
list_1, list_2, winners = [], [], []

for i in range(players_qty):
    list_1.append(round(random.uniform(5, 10),2))
    list_2.append(round(random.uniform(5, 10),2))

# Также можно в виде генератора списка:
# list_1 = [round(random.uniform(5, 10), 2) for _ in range(players_qty)]
# list_2 = [round(random.uniform(5, 10), 2) for _ in range(players_qty)]

for i_player in range(players_qty):
    if list_1[i_player] > list_2[i_player]:
        winners.append(list_1[i_player])
    else:
        winners.append(list_2[i_player])

# Также можно в виде генератора списка:
# winners = [
#     list_1[i_player] if list_1[i_player] > list_2[i_player]
#     else list_2[i_player]
#     for i_player in range(players_qty)
# ]

print(list_1)
print(list_2)
print(winners)