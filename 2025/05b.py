# https://adventofcode.com/2025/day/5

lines = open(0).readlines()
ranges = [[int(n) for n in line.split('-')] for line in lines[:lines.index('\n')]]
for i, range0 in enumerate(ranges):
    for j, range1 in enumerate(ranges[i + 1:], start=i + 1):
        if range0[1] >= range1[0] and range0[0] <= range1[1]:
            ranges[i] = [1, 0]
            ranges[j] = [min(range0[0], range1[0]), max(range0[1], range1[1])]
            break
print(sum([range_[1] - range_[0] for range_ in ranges]) + len(ranges))