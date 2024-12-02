# https://adventofcode.com/2024/day/1#part2

lists = [[int(x) for x in line.split()] for line in open(0)]
list2 = [line[1] for line in lists]
print(sum([line[0] * list2.count(line[0]) for line in lists]))

