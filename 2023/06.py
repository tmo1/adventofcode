# https://adventofcode.com/2023/day/6

times, distances = [[int(n) for n in line.split()[1:]] for line in open(0)]
ways = 1
for race in range(len(times)):
    ways *= sum([1 for press_time in range(1, times[race]) if press_time * (times[race] - press_time) > distances[race]])
print(ways)
