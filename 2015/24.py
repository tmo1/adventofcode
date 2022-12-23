# https://adventofcode.com/2015/day/24

import sys

packages = []
for line in sys.stdin:
    packages.append(int(line))
weight = sum(packages) // 3
g = set()


def groups(n, last_package, selected_packages):
    global g
    s = sum(selected_packages)
    if n == 0:
        if s == weight:
            g.add(tuple(selected_packages))
    elif s <= weight:
        for i in range(last_package + 1, len(packages)):
            groups(n - 1, i, selected_packages + [packages[i]])


count = 0
while True:
    count += 1
    groups(count, -1, [])
    if len(g) > 0:
        quantum = 1000000000000
        for group in g:
            prod = 1
            for package in group:
                prod *= package
            quantum = min(quantum, prod)
        print(quantum)
        exit()
