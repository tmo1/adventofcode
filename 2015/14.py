# https://adventofcode.com/2015/day/14#part2

import sys

reindeer = []
farthest = 0
for line in sys.stdin:
    words = line.split()
    distance = ((2503 // (int(words[6]) + int(words[13]))) * int(words[3]) * int(words[6])) + (
                int(words[3]) * min(int(words[6]), 2503 % (int(words[6]) + int(words[13]))))
    if distance > farthest:
        farthest = distance
print(farthest)
