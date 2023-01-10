# https://adventofcode.com/2016/day/22

import sys

nodes, viable = [], 0
sys.stdin.readline()
sys.stdin.readline()
for line in sys.stdin:
    line = line.split()
    nodes.append((int(line[2][:-1]), int(line[3][:-1])))
for node_a in nodes:
    for node_b in nodes:
        if node_a != node_b and node_a[0] != 0 and node_b[1] >= node_a[0]:
            viable += 1
print(viable)
