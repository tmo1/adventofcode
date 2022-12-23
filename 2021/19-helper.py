#! /usr/bin/python3

# https://adventofcode.com/2021/day/19

orients = {}

def rotatez(x):
	return (x[1], -x[0], x[2])

def rotatex(x):
	return (x[0], x[2], -x[1])

def rotatey(x):
	return (x[2], x[1], -x[0])

q = (1, 2, 3)
for i in range(4):
	q = rotatex(q)
	for j in range(4):
		q = rotatey(q)
		for k in range(4):
			q = rotatez(q)
			if q not in orients:
				orients[q] = [(i + 1, j + 1, k + 1)]
			else:
				orients[q].append((i + 1, j + 1, k + 1))
#print(len(orients))
orient_list = []
for orient in orients:
	print((orient), orients[orient])
	orient_list.append(tuple(map(lambda x: x % 4, orients[orient][0])))
print(orient_list)
