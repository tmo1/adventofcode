# https://adventofcode.com/2015/day/17#part2

import sys

containers = [int(line) for line in sys.stdin]
min_containers = len(containers)
ways = {}


def add_container(subtotal, i, c):
    if not subtotal > 150:
        global min_containers
        global ways
        if i == len(containers):
            if subtotal == 150:
                if c < min_containers:
                    min_containers = c
                    ways[min_containers] = 1
                elif c == min_containers:
                    ways[min_containers] += 1
        else:
            add_container(subtotal + containers[i], i + 1, c + 1)
            add_container(subtotal, i + 1, c)


add_container(0, 0, 0)
print(ways[min_containers])
