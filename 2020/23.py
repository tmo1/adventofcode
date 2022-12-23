#! /usr/bin/python3

# https://adventofcode.com/2020/day/23

cups = [3,8,9,1,2,5,4,6,7]
#cups = [3,8,9,5,4,7,6,1,2]
for i in range(100):
	three = cups[1:4]
	cups[1:4] = []
	dest = cups[0] - 1
	while not dest in cups:
		if dest == 0:
			dest = 10
		dest -= 1
	cups[cups.index(dest) + 1:cups.index(dest) + 1] = three
	cups.append(cups.pop(0))
string = ''
for i in range(cups.index(1) + 1, cups.index(1) + 9):
	print(i)
	string = string + str(cups[i % 9])
print(string)
