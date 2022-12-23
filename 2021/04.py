#! /usr/bin/python3

# https://adventofcode.com/2021/day/4

import sys

nums = sys.stdin.readline().split(',')
boards = []
while sys.stdin.readline():
	board = []
	for i in range(5):
		line = sys.stdin.readline().split()
		board.append(line)
	boards.append(board)
for num in nums:
	for board in boards:
		for i in range(5):
			for j in range(5):
				if board[i][j] == num:
					board[i][j] = '*'
					x = 0
					y = 0
					for k in range(5):
						if board[i][k] == '*':
							x += 1
						if board[k][j] == '*':
							y += 1
					if x == 5 or y == 5:
						s = 0
						for l in range(5):
							for m in range(5):
								if board[l][m] != '*':
									s += int(board[l][m])
						print(s * int(num))
						quit()
