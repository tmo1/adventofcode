#! /usr/bin/python3

# https://adventofcode.com/2021/day/12

import sys

connections = []
visited = set()

for line in sys.stdin:
	connections.append(line.strip().split('-'))
paths = 0

def extend(cave):
	global paths, visited
	if cave == 'end':
		paths += 1
	else:
		if cave.islower():
			visited.add(cave)
		for connection in connections:
			if connection[0] == cave and (connection[1] not in visited or connection[1].isupper()):
				extend(connection[1])
			elif connection[1] == cave and (connection[0] not in visited or connection[0].isupper()):
				extend(connection[0])
		if cave.islower():
			visited.remove(cave)

extend('start')
print(paths)
