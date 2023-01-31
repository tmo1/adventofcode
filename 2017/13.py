# https://adventofcode.com/2017/day/13
# the solution for part 2 utilizes simpler and shorter logic than this solution

import sys
from collections import defaultdict

firewall, packet, severity = defaultdict(lambda: [0, -1, 1]), 0, 0
for line in sys.stdin:
    line = line.split(': ')
    firewall[int(line[0])] = [int(line[1]), 0, 1]
firewall_end = max(firewall.keys())
while packet <= firewall_end:
    if firewall[packet][1] == 0:
        severity += packet * firewall[packet][0]
    for layer in firewall.values():
        layer[1] += layer[2]
        if layer[1] == 0 or layer[1] == layer[0] - 1:
            layer[2] = -layer[2]
    packet += 1
print(severity)
