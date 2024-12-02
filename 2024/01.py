# https://adventofcode.com/2024/day/1

lists = [[int(x) for x in line.split()] for line in open(0)]
print(sum([abs(a - b) for a, b in zip(sorted([line[0] for line in lists]), sorted([line[1] for line in lists]))]))
