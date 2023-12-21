# https://adventofcode.com/2023/day/17

import itertools
from heapq import heappop, heappush
from collections import defaultdict

# https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


heat_map = [[int(n) for n in line.strip()] for line in open(0)]
movement = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
for y in range(len(heat_map)):
    for x in range(len(heat_map[0])):
        for direction in range(4):
            for consecutive in range(1, 4):
                add_task((x, y, direction, consecutive), 1000000)
add_task((0, 0, 1, 0))
total_heat = defaultdict(lambda: 1000000)
total_heat[(0, 0, 1, 0)] = 0
while True:
    t = pop_task()
    x, y, direction, consecutive = t
    if x == len(heat_map[0]) - 1 and y == len(heat_map) - 1:
        print(total_heat[t])
        quit()
    neighbors = [((direction + 1) % 4, 1), ((direction - 1) % 4, 1)]
    if consecutive < 3:
        neighbors.append((direction, consecutive + 1))
    for neighbor in neighbors:
        new_direction, new_consecutive = neighbor
        new_x, new_y = x + movement[new_direction][0], y + movement[new_direction][1]
        new_t = (new_x, new_y, new_direction, new_consecutive)
        if 0 <= new_x < len(heat_map[0]) and 0 <= new_y < len(heat_map):
            new_heat = total_heat[t] + heat_map[new_y][new_x]
            if new_heat < total_heat[new_t]:
                total_heat[new_t] = new_heat
                add_task(new_t, new_heat)
