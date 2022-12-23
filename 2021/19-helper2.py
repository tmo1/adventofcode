#! /usr/bin/python3

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
print(transformations, '\n', len(transformations))
