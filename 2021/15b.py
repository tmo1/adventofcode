#! /usr/bin/python3

# https://adventofcode.com/2021/day/15#part2

import sys
import heapq
import itertools

grid = []
for line in sys.stdin:
	line = [int(c) for c in line[:-1]]
	line5 = []
	for i in range(5):
		for n in line:
			line5.append(((n + i - 1) % 9) + 1)
	grid.append(line5)
grid5 = []
for i in range(5):
	for j in range(len(grid)):
		line = []
		for k in range(len(grid) * 5):
			line.append(((grid[j][k] + i - 1) % 9) + 1)
		grid5.append(line)
grid = grid5
side = len(grid)

risks = [[1000000 for i in range(side)] for j in range(side)]

# https://docs.python.org/3/library/heapq.html
pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count() # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

for i in range(side):
	for j in range(side):
		add_task((i, j), 1000000)

risks[0][0] = 0
add_task((0, 0), 0)

while True:
	x, y = pop_task()
	for x1 in range(max(x - 1, 0), min(x + 2, side)):
		for y1 in range(max(y - 1, 0), min(y + 2, side)):
			if (x1 == x and y1 != y) or (y1 == y and x1 != x):
				r = risks[y][x] + grid[y1][x1]
				if r < risks[y1][x1]:
					risks[y1][x1] = r
					add_task((x1, y1), r)
	if x == side -1 and y == side - 1:
		print(risks[y1][x1])
		quit()
