# https://adventofcode.com/2015/day/17

import sys

containers = [int(line) for line in sys.stdin]
min_containers = 0


def add_container(subtotal, i):
    if not subtotal > 150:
        global min_containers
        if i == len(containers):
            if subtotal == 150:
                ways += 1
        else:
            add_container(subtotal + containers[i], i + 1)
            add_container(subtotal, i + 1)


add_container(0, 0)
print(min_containers)
