# Самая далекая планета
from math import pi

def find_farthest_orbit(list_of_orbits):
    list_without_sputnics = [i for i in list_of_orbits if i[0] != i[1]]
    print(list_without_sputnics)

    list_s = [(pi * i[0] * i[1]) for i in list_without_sputnics]
    max_index = list_s.index(max(list_s))

    return list_without_sputnics[max_index]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit(orbits))