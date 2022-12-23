#! /usr/bin/python3

# https://adventofcode.com/2020/day/13

f = open('aoc-input', 'r')
#f = open('sample', 'r')
t1 = int(f.readline())
line = f.readline()
ids = line.split(',')
buses = []
for i in ids:
	if i == 'x':
		continue
	buses.append(int(i))
t2 = t1
while 1:
	for b in buses:
		if t2 % b == 0:
			print((t2 - t1) * b)
			raise SystemExit
	t2 +=1
