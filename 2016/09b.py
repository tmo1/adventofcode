# https://adventofcode.com/2016/day/9#part2

import sys


def decompress(sequence):
    i, marker, prev, total = 0, False, [], 0
    while i < len(sequence):
        match sequence[i]:
            case '(':
                marker = True
            case ')':
                seq, multiply = ''.join(prev).split('x')
                seq, multiply = int(seq), int(multiply)
                new_sequence = sequence[i + 1:i + 1 + seq]
                total += multiply * decompress(new_sequence)
                i = i + seq
                marker = False
                prev = []
            case other:
                if marker is False:
                    total += 1
                else:
                    prev.append(sequence[i])
        i += 1
    return total


print(decompress(sys.stdin.readline().strip()))
