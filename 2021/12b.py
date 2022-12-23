#! /usr/bin/python3

# https://adventofcode.com/2021/day/12#part2

import sys

connections = []
visited = set()

for line in sys.stdin:
	connections.append(line.strip().split('-'))

paths = 0
twice = ''

def extend(cave):
	global paths, visited, twice
	if cave == 'end':
		paths += 1
	else:
		if cave.islower():
			visited.add(cave)
		for connection in connections:
			if connection[0] == cave:
				if connection[1] not in visited or connection[1].isupper():
					extend(connection[1])
				elif twice == '' and connection[1] != 'start':
					twice = connection[1]
					extend(connection[1])
					twice = ''
			elif connection[1] == cave:
				if connection[0] not in visited or connection[0].isupper():
					extend(connection[0])
				elif twice == '' and connection[0] != 'start':
						twice = connection[0]
						extend(connection[0])
						twice = ''
		if cave.islower() and twice != cave:
			visited.remove(cave)

extend('start')
print(paths)
