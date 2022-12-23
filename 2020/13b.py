#! /usr/bin/python3

# https://adventofcode.com/2020/day/13

# Note that this solution to part 2 assumes that all the bus numbers
# are relatively prime, which is not specified in the puzzle, but is
# the case in our input

f = open('aoc-input', 'r')
#f = open('sample', 'r')
line = f.readline()
line = f.readline()
ids = line.split(',')
buses = []
for i in ids:
	buses.append(0 if i == 'x' else int(i))
period = buses[0]
first = 0
for i in range(1, len(buses)):
	if buses[i] == 0:
		continue
	t = first
	while 1:
		if (t + i) % buses[i] == 0:
			break
		t += period
	period *= buses[i]
	first = t
print(first)
