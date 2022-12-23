# https://adventofcode.com/2015/day/9

import sys
distances = {}
cities = set()
shortest = 0
for line in sys.stdin:
    words = line.split()
    distances[(words[0], words[2])] = distances[(words[2], words[0])] = int(words[-1])
    shortest += int(words[-1])
    cities |= {words[0], words[2]}


def calc(last_city, distance, remaining_cities):
    global shortest
    for city in remaining_cities:
        new_distance = distance + distances[(last_city, city)]
        if new_distance > shortest:
            continue
        if len(remaining_cities) == 1:
            shortest = new_distance
        else:
            calc(city, new_distance, remaining_cities - {city})


for c in cities:
    calc(c, 0, cities - {c})
print(shortest)
