#! /usr/bin/python3

# https://adventofcode.com/2021/day/23

import sys
from math import inf
from copy import deepcopy

homes = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
energies = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
min_energy = inf

# def display(burrow):
	# for line in burrow:
		# print(''.join(line))
	# print()

def move(burrow, energy):
	for x in list(homes.values()):
		for y in [2, 3]:
			if burrow[y][x] == '.' or homes[burrow[y][x]] != x:
				break
		else:
			continue
		break
	else:
		global min_energy
		# if energy < min_energy:
			# print('new min_energy found: ', energy)
		min_energy = min(energy, min_energy)
		return
	
	for x in [1, 2, 4, 6, 8, 10, 11]:
		a = burrow[1][x]
		if a.isalpha() and burrow[2][homes[a]] == '.' and (burrow[3][homes[a]] == '.' or burrow[3][homes[a]] == a) and all(burrow[1][k] == '.' for k in range(homes[a], x, 1 if x > homes[a] else -1)):
			e = energies[a] * (abs(x - homes[a]) + (2 if burrow[3][homes[a]] == '.' else 1))
			if energy + e < min_energy:
				new_burrow = deepcopy(burrow)
				new_burrow[1][x] = '.'
				new_burrow[2 if burrow[3][homes[a]] == a else 3][homes[a]] = a
				move(new_burrow, energy + e)
			return
	for x in list(homes.values()):
		out = 0
		if burrow[2][x].isalpha() and burrow[3][x].isalpha() and (homes[burrow[3][x]] != x or homes[burrow[2][x]] != x):
			out = 2
		elif burrow[3][x].isalpha() and burrow[2][x] == '.' and homes[burrow[3][x]] != x:
			out = 3
		if out > 0:
			for x2 in [1, 2, 4, 6, 8, 10, 11]:
				if all(burrow[1][k] == '.' for k in range(x, x2 + (1 if x2 > x else -1), 1 if x2 > x else -1)):
					e = energies[burrow[out][x]] * (abs(x - x2) + (2 if out == 3 else 1))
					if energy + e < min_energy:
						new_burrow = deepcopy(burrow)
						new_burrow[1][x2] = burrow[out][x]
						new_burrow[out][x] = '.'
						move(new_burrow, energy + e)
	return

burrow = []
for line in sys.stdin:
	burrow.append(list(line.strip()))
for i in range(3, 5):
	burrow[i] = [' ',' '] + burrow[i]

move(burrow, 0)
print(min_energy)

