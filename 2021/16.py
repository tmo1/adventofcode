#! /usr/bin/python3

# https://adventofcode.com/2021/day/16

import sys

msg = sys.stdin.readline().strip()
bits = []
for digit in msg:
	bits += f'{int(digit, 16):04b}'
bits.reverse()
version_sum = 0

def parse(data):
	version = int(''.join(data.pop() for i in range(3)), 2)
	global version_sum
	version_sum += version
	type_id = int(''.join(data.pop() for i in range(3)), 2)
	if type_id == 4:
		while True:
			flag = data.pop()
			for i in range(4):
				data.pop()
			if flag == '0':
				break
	else:
		if data.pop() == '0':
			length = int(''.join(data.pop() for i in range(15)), 2)
			curlength = len(data)
			while curlength - len(data) < length:
				parse(data)
		else:
			num = int(''.join(data.pop() for i in range(11)), 2)
			for i in range(num):
				parse(data)

parse(bits)
print(version_sum)
