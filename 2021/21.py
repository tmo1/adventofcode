#! /usr/bin/python3

# https://adventofcode.com/2021/day/19

import sys

rolls = 0
die = 0
players = [[int(sys.stdin.readline().split()[-1]), 0], [int(sys.stdin.readline().split()[-1]), 0]]

def roll():
	global rolls, die
	rolls += 1
	die = die % 100 + 1
	return die

while players[1][1] < 1000:
	players[0][0] = ((players[0][0] + roll() + roll() + roll() - 1) % 10) + 1
	players[0][1] += players[0][0]
	players[0], players[1] = players[1], players[0]

print(players[0][1] * rolls)
