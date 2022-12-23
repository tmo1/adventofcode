#! /usr/bin/python3

# https://adventofcode.com/2021/day/6#part2

import sys

fish = sys.stdin.readline().split(',')
for i in range(len(fish)):
	fish[i] = int(fish[i])
fish2 = [0] * 9
for f in fish:
	fish2[f] += 1

for i in range(256):
	fish3 = [0] * 9
	for j in range(1,9):
		fish3[j - 1] = fish2[j]
	fish3[6] += fish2[0]
	fish3[8] = fish2[0]
	fish2 = fish3

print(sum(fish2))
