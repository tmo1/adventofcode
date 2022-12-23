#! /usr/bin/python3

# https://adventofcode.com/2020/day/25

def transform(subnum, loop):
	n = 1
	for i in range(loop):
		n = (n * subnum) % 20201227
	return n

def brute(x):
	n = 1
	for i in range(10000000):
		n = (n * 7) % 20201227
		if n == x:
			return(i + 1)

loop1 = brute(1327981)
loop2 = brute(2822615)
print(transform(1327981, loop2))
