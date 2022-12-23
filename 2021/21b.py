#! /usr/bin/python3

# https://adventofcode.com/2021/day/21#part2

import sys

dirac = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
known = {}

def move(space, n):
	return ((space + n - 1) % 10) + 1

def universes(p1space, p1score, p2space, p2score, turn):
	if (p1space, p1score, p2space, p2score, turn) in known:
		return known[(p1space, p1score, p2space, p2score, turn)]
	u = [0, 0]
	if turn == 1:
		for n in dirac:
			if p1score + move(p1space, n) >= 21:
				u[0] += dirac[n]
			else:
				u1 = universes(move(p1space, n), p1score + move(p1space, n), p2space, p2score, 2)
				u[0] += dirac[n] * u1[0]
				u[1] += dirac[n] * u1[1]
	else:
		for n in dirac:
			if p2score + move(p2space, n) >= 21:
					u[1] += dirac[n]
			else:
				u1 = universes(p1space, p1score, move(p2space, n), p2score + move(p2space, n), 1)
				u[0] += dirac[n] * u1[0]
				u[1] += dirac[n] * u1[1]
	known[(p1space, p1score, p2space, p2score, turn)] = u
	return u

u = universes(int(sys.stdin.readline().split()[-1]), 0, int(sys.stdin.readline().split()[-1]), 0, 1)
print(max(u[0], u[1]))
