# https://adventofcode.com/2022/day/15#part2
# This takes about 45 seconds (for my input) on my ThinkPad W550s

import sys
import re

beacon_reports = []
for line in sys.stdin:
    line = re.split('[ =]', line)
    beacon_reports.append(list(map(lambda n: int(n), [line[3].strip(','), line[5].strip(':'), line[11].strip(','), line[13].strip()])))
for y in range(4000001):
    eliminated_ranges = []
    for beacon_report in beacon_reports:
        distance_difference = abs(beacon_report[2] - beacon_report[0]) + abs(beacon_report[3] - beacon_report[1]) - abs(beacon_report[1] - y)
        if distance_difference >= 0:
            eliminated_ranges.append((beacon_report[0] - distance_difference, beacon_report[0] + distance_difference))
    location = 0
    while location < 4000001:
        for eliminated_range in eliminated_ranges:
            if eliminated_range[0] <= location <= eliminated_range[1]:
                location = eliminated_range[1] + 1
                break
        else:
            print((location * 4000000) + y)
            quit()
