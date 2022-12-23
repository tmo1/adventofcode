#! /usr/bin/python3

# https://adventofcode.com/2020/day/11

seats = []
f = open('aoc-input', 'r')
while row := f.readline():
	seats.append(list(row.rstrip()))
x, y = len(seats[0]), len(seats)
def check(i, j):
	if i == -1 or i == x or j == -1 or j == y:
		return 0
	return 1 if seats[j][i] == '#' else 0
stable = 0
while not stable:
	new_seats = [[0 for i in range(x)] for j in range(y)] 
	stable = 1
	for i in range(0, x):
		for j in range(0, y):
			neighbors = 0
			for k in [i - 1, i, i + 1]:
				for l in [j - 1, j, j + 1]:
					if k != i or l != j:
						neighbors += check(k, l)
			if seats[j][i] == 'L' and neighbors == 0:
				new_seats[j][i] = '#'
				stable = 0
			elif seats[j][i] == '#' and neighbors > 3:
				new_seats[j][i] = 'L'
				stable = 0
			else:
				new_seats[j][i] = seats[j][i]
	seats = new_seats
total = 0
for i in range(0, x):
	for j in range(0, y):
		if seats[j][i] == '#':
			total += 1
print(total)
