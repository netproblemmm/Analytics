# Задача 3. Турнир
import os

os.chdir('D:/Projects/Analytics/01-12') 

first_tour_file = open('01-12_HW-3_first_tour.txt', 'r')
lines = first_tour_file.readlines()
first_tour_file.close()

k = int(lines[0].strip())
players_list = {}
winners_list = {}

for line in lines[1:]:
    data = line.strip().split()
    name = f'{data[1][0]}. {data[0]}'
    score = int(data[2])
    players_list[name] = score

for player, score in players_list.items():
    if score > k:
        winners_list[player] = score

winners_list = dict(sorted(winners_list.items(), key = lambda x: x[1], reverse=True))

count = 1

second_tour_file = open('01-12_HW-3_second_tour.txt', 'w')
second_tour_file.write(f'{len(winners_list)}\n')

for winner, score in winners_list.items():
    second_tour_file.write(f'{count}) {winner} {score}\n')
    count += 1