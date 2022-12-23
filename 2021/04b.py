#! /usr/bin/python3

# https://adventofcode.com/2021/day/4#part2

import sys

nums = sys.stdin.readline().split(',')
boards = []
while sys.stdin.readline():
	board = []
	for i in range(5):
		line = sys.stdin.readline().split()
		board.append(line)
	boards.append(board)
won = ['n'] * len(boards)
remaining = len(boards)
for num in nums:
	for n in range(len(boards)):
		if won[n] == 'y':
			continue
		for i in range(5):
			for j in range(5):
				if boards[n][i][j] == num:
					boards[n][i][j] = '*'
					x = 0
					y = 0
					for k in range(5):
						if boards[n][i][k] == '*':
							x += 1
						if boards[n][k][j] == '*':
							y += 1
					if x == 5 or y == 5:
						won[n] = 'y'
						remaining -= 1
						if remaining == 0:
							s = 0
							for l in range(5):
								for m in range(5):
									if boards[n][l][m] != '*':
										s += int(boards[n][l][m])
							print(s * int(num))
							quit()
