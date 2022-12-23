# https://adventofcode.com/2022/day/7

import sys


class Node:
    def __init__(self, size, name, parent):
        self.children = []
        self.size = size
        self.name = name
        self.parent = parent


root = Node(0, '/', None)
total = 0
for line in sys.stdin:
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                cur = root
            elif line[2] == '..':
                cur = cur.parent
            else:
                for child in cur.children:
                    if child.name == line[2]:
                        cur = child
        elif line[1] == 'ls':
            continue
    else:
        cur.children.append(Node(0 if line[0] == 'dir' else int(line[0]), line[1], cur))


def walk(node):
    global total
    if len(node.children) == 0:
        return node.size
    sub_total = sum([walk(x) for x in node.children])
    if sub_total <= 100000:
        total += sub_total
    return sub_total


walk(root)
print(total)
