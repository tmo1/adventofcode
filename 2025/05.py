# https://adventofcode.com/2025/day/5

lines = open(0).readlines()
ranges = [[int(n) for n in line.split('-')] for line in lines[:lines.index('\n')]]
print(sum([1 for line in lines[lines.index('\n') + 1:] if sum([1 for range_ in ranges if range_[0] <= int(line) <= range_[1]]) > 0]))