#! /usr/bin/python3

f = open('input', 'r')
valid = 0
while line := f.readline():
	prange, letter, password = line.split()
	letter = letter[0]
	minimum, maximum = prange.split('-')
	minimum, maximum = int(minimum), int(maximum)
	if password.count(letter) >= minimum and password.count(letter) <= maximum:
		valid += 1
print(valid)
