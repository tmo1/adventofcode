# https://adventofcode.com/2022/day/15

import sys
import re

no_beacons = set()
for line in sys.stdin:
    line = re.split('[ =]', line)
    coordinates = list(map(lambda x: int(x), [line[3].strip(','), line[5].strip(':'), line[11].strip(','), line[13].strip()]))
    distance_difference = abs(coordinates[2] - coordinates[0]) + abs(coordinates[3] - coordinates[1]) - abs(coordinates[1] - 2000000)
    if distance_difference >= 0:
        for i in range(distance_difference + 1):
            if (coordinates[2], coordinates[3]) != (coordinates[0] - i, 2000000):
                no_beacons.add(coordinates[0] - i)
            if (coordinates[2], coordinates[3]) != (coordinates[0] + i, 2000000):
                no_beacons.add(coordinates[0] + i)
print(len(no_beacons))
