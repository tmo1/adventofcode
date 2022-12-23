#! /usr/bin/python3

# https://adventofcode.com/2021/day/23#part2

import sys
from math import inf

homes = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
energies = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
min_energy = inf

def switch(burrow, x1, y1, x2, y2):
	burrow[y1][x1], burrow[y2][x2] = burrow[y2][x2], burrow[y1][x1]
	
def move(burrow, energy):
	for x in list(homes.values()):
		for y in range(2, 6):
			if burrow[y][x] == '.' or homes[burrow[y][x]] != x:
				break
		else:
			continue
		break
	else:
		global min_energy
		if energy < min_energy:
			print('new min_energy found: ', energy)
		min_energy = min(energy, min_energy)
		return
	
	for x in [1, 2, 4, 6, 8, 10, 11]:
		a = burrow[1][x]
		if a != '.' and all((burrow[n][homes[a]] == '.' or burrow[n][homes[a]] == a) for n in range(2, 6)) and all(burrow[1][k] == '.' for k in range(homes[a], x, 1 if x > homes[a] else -1)):
			for i in range(5, 1, -1):
				if burrow[i][homes[a]] == '.':
					break
			e = energies[a] * (abs(x - homes[a]) + i - 1)
			if energy + e < min_energy:
				switch(burrow, x, 1, homes[a], i)
				move(burrow, energy + e)
				switch(burrow, homes[a], i, x, 1)
			return
	for x in list(homes.values()):
		if any((burrow[n][x] != '.' and homes[burrow[n][x]] != x) for n in range(2, 6)):
			for out in range(2, 6):
				if burrow[out][x] != '.':
					break
			for x2 in [1, 2, 4, 6, 8, 10, 11]:
				if all(burrow[1][k] == '.' for k in range(x, x2 + (1 if x2 > x else -1), 1 if x2 > x else -1)):
					e = energies[burrow[out][x]] * (abs(x - x2) + out - 1)
					if energy + e < min_energy:
						switch(burrow, x, out, x2, 1)
						move(burrow, energy + e)
						switch(burrow, x2, 1, x, out)
	return

burrow = []
for line in sys.stdin:
	burrow.append(list(line.strip()))
for i in [3, 4]:
	burrow[i] = [' ',' '] + burrow[i]
burrow = burrow[:3] + [list('  #D#C#B#A#'), list('  #D#B#A#C#')] + burrow[3:]
move(burrow, 0)
print(min_energy)

