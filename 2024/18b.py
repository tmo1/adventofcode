# https://adventofcode.com/2024/day/18#part2

import itertools
from heapq import heappush, heappop
from re import findall

# https://docs.python.org/3/library/heapq.html

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

mem_bytes = [int(n) for n in findall(r"\d+", open(0).read())]
directions= {(0, 1), (0, -1), (1, 0), (-1, 0)}
yes_path, no_path = 0, len(mem_bytes) // 2 - 1
while yes_path < no_path - 1:
    try_path = (yes_path + no_path) // 2
    space = [[[1000000, True] for x in range(71)] for y in range(71)]
    for i in range(0, try_path + 1):
        space[mem_bytes[i * 2 + 1]][mem_bytes[i * 2]][1] = False
    pq = []  # list of entries arranged in a heap
    entry_finder = {}  # mapping of tasks to entries
    for y in range(71):
        for x in range(71):
            add_task((x, y), 1000000)
    add_task((0, 0), 0)
    space[0][0][0] = 0
    while True:
        x, y = pop_task()
        if x == 70 and y == 70:
            if space[70][70][0] < 1000000:
                yes_path = try_path
            else:
                no_path = try_path
            break
        for direction in directions:
            x1, y1 = x + direction[0], y + direction[1]
            if 0 <= x1 < 71 and 0 <= y1 < 71 and space[y][x][0] + 1 < space[y1][x1][0] and space[y1][x1][1]:
                space[y1][x1][0] = space[y][x][0] + 1
                add_task((x1, y1), space[y][x][0] + 1)
        space[y][x][1] = False
print(mem_bytes[no_path * 2], ',', mem_bytes[no_path * 2 + 1], sep='')
