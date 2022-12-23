#! /usr/bin/python3

# https://adventofcode.com/2021/day/6

import sys

fish = sys.stdin.readline().split(',')
for i in range(len(fish)):
	fish[i] = int(fish[i])
for i in range(80):
	n = len(fish)
	for j in range(n):
		if fish[j] == 0:
			fish[j] = 6
			fish.append(8)
		else:
			fish[j] -= 1
print(len(fish))
