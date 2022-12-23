#! /usr/bin/python3

# https://adventofcode.com/2021/day/19
# one empty line needs to be appended to the input for this to run

import sys
from collections import defaultdict
sensors = []
beacons = set()

def rotatez(x):
	return (x[1], (x[0][0], 1 - x[0][1]), x[2])

def rotatex(x):
	return (x[0], x[2], (x[1][0], 1 - x[1][1]))

def rotatey(x):
	return (x[2], x[1], (x[0][0], 1 - x[0][1]))

rotation = ((0, 1), (1, 1), (2, 1))
transformations = set()
for i in range(4):
	rotation = rotatex(rotation)
	for j in range(4):
		rotation = rotatey(rotation)
		for k in range(4):
			rotation = rotatez(rotation)
			transformations.add(rotation)

def transform(beacon, transformation):
	return (beacon[transformation[0][0]] if transformation[0][1] == 1 else -beacon[transformation[0][0]], beacon[transformation[1][0]] if transformation[1][1] == 1 else -beacon[transformation[1][0]], beacon[transformation[2][0]] if transformation[2][1] == 1 else -beacon[transformation[2][0]])
	
def diff(x, y):
	return (x[0] - y[0], x[1] - y[1], x[2] - y[2])

for line in sys.stdin:
	if line[0] == '\n':
		sensors.append(beacons)
		beacons = set()
	elif line[-2] != '-':
		x, y, z = line.split(',')
		beacons.add((int(x), int(y), int(z)))
	
while len(sensors) > 1:
	#print(len(sensors), 'sensors remaining')
	for i in range(len(sensors) - 1):
		for j in range(i + 1, len(sensors)):
			for transformation in transformations:
				beacon_set = set(map(lambda x: transform(x, transformation), sensors[j]))
				diffs = defaultdict(lambda: 0)
				for beacon2 in beacon_set:
					for beacon1 in sensors[i]:
						d = diff(beacon2, beacon1)
						diffs[d] += 1
						if diffs[d] == 12:
							break
					else:
						continue
					break
				else:
					continue
				break
			else:
				continue
			#print('found overlap between ', i, j)
			sensors[i] |= set(map(lambda x: diff(x, d), beacon_set))
			sensors.pop(j)
			break
		else:
			continue
		break

print(len(sensors[0]))
