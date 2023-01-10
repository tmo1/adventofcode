# https://adventofcode.com/2016/day/8#part2

import sys

prev, compressed, decompressed, marker = [], sys.stdin.readline().strip(), [], False
i = 0
while i < len(compressed):
    match compressed[i]:
        case '(':
            marker = True
        case ')':
            seq, multiply = ''.join(prev).split('x')
            seq, multiply = int(seq), int(multiply)
            for j in range(multiply):
                decompressed += compressed[i + 1:i + 1 + seq]
            i = i + seq
            marker = False
            prev = []
        case other:
            if marker is False:
                decompressed.append(compressed[i])
            else:
                prev.append(compressed[i])
    i += 1
print(len(decompressed))
