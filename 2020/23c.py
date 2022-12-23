#! /usr/bin/python3

# https://adventofcode.com/2020/day/23
# input is hard-coded into the 'start' assignment

cups = {}
NUM = 1000000
start = [3,8,9,5,4,7,6,1,2] + [i for i in range(10, NUM + 1)]
for i in range(len(start) - 1):
	cups[start[i]] = start[(i + 1)]
cups[start[-1]] = start[0]
current = 3

for i in range(10000000):
	one = cups[current]
	two = cups[one]
	three = cups[two]
	cups[current] = cups[three]
	dest = current - 1
	while dest in [one, two, three] or dest == 0:
		if dest == 0:
			dest = NUM
		else:
			dest -= 1
	x = cups[dest]
	cups[dest] = one
	cups[three] = x
	current = cups[current]

print(cups[1] * cups[cups[1]])
