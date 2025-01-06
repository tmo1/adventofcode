# https://adventofcode.com/2024/day/18

# https://docs.python.org/3/library/heapq.html

import itertools
from heapq import heappush, heappop

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

space = [[[1000000, True] for x in range(71)] for y in range(71)]
directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
for line in open(0).readlines()[:1024]:
    x, y = [int(n) for n in line.split(',')]
    space[y][x][0] = -1
for y in range(71):
    for x in range(71):
        add_task((x, y), 1000000)
add_task((0, 0), 0)
space[0][0][0] = 0
while True:
    x, y = pop_task()
    if x == 70 and y == 70:
        print(space[70][70][0])
        quit()
    for direction in directions:
        x1, y1 = x + direction[0], y + direction[1]
        if 0 <= x1 < 71 and 0 <= y1 < 71 and space[y][x][0] < space[y1][x1][0] - 1 and space[y1][x1][1]:
            space[y1][x1][0] = space[y][x][0] + 1
            add_task((x1, y1), space[y][x][0] + 1)
    space[y][x][1] = False
