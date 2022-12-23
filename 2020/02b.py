#! /usr/bin/python3

f = open('input', 'r')
valid = 0
while line := f.readline():
	prange, letter, password = line.split()
	letter = letter[0]
	minimum, maximum = prange.split('-')
	minimum, maximum = int(minimum) -1, int(maximum) - 1
	if (password[minimum] == letter and password[maximum] != letter) or (password[maximum] == letter and password[minimum] != letter):
		valid += 1
print(valid)
