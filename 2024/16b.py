# https://adventofcode.com/2024/day/16#part2

# https://docs.python.org/3/library/heapq.html

import itertools
from heapq import heappop, heappush

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

maze, directions = open(0).read().split(), {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
for y in range(1, len(maze) - 1):
    for x in range(1, len(maze[0]) - 1):
        for i in range(4):
            add_task((x, y, i), 1000000)
maze_values = [[[[1000000, False] for i in range(4)] for x in range(len(maze[0]))] for y in range(len(maze))]
maze_values[len(maze) - 2][1][1][0] = 0
add_task((1, len(maze) - 2, 1), 0)
while True:
    x, y, d = pop_task()
    if (x, y) == (len(maze[0]) - 2, 1):
        break
    if maze[y + directions[d][1]][x + directions[d][0]] in ['.', 'E'] and maze_values[y][x][d][0] + 1 < maze_values[y + directions[d][1]][x + directions[d][0]][d][0] and not maze_values[y + directions[d][1]][x + directions[d][0]][d][1]:
        maze_values[y + directions[d][1]][x + directions[d][0]][d][0] = maze_values[y][x][d][0] + 1
        add_task((x + directions[d][0], y + directions[d][1], d), maze_values[y][x][d][0] + 1)
    if maze_values[y][x][d][0] + 1000 < maze_values[y][x][(d + 1) % 4][0] and not maze_values[y][x][(d + 1) % 4][1]:
        maze_values[y][x][(d + 1) % 4][0] = maze_values[y][x][d][0] + 1000
        add_task((x, y, (d + 1) % 4), maze_values[y][x][d][0] + 1000)
    if maze_values[y][x][d][0] + 1000 < maze_values[y][x][(d - 1) % 4][0] and not maze_values[y][x][(d - 1) % 4][1]:
        maze_values[y][x][(d - 1) % 4][0] = maze_values[y][x][d][0] + 1000
        add_task((x, y, (d - 1) % 4), maze_values[y][x][d][0] + 1000)
    maze_values[y][x][d][1] = True
# https://math.stackexchange.com/a/998883
tiles, tiles_ = [(x, y, d, maze_values[y][x][d][0])], set()
while tiles:
    x, y, d, score = tile = tiles.pop()
    if maze[y - directions[d][1]][x - directions[d][0]] in ['.', 'S'] and score - 1 == maze_values[y - directions[d][1]][x - directions[d][0]][d][0]:
        tiles.append((x - directions[d][0], y - directions[d][1], d, score - 1))
    if maze_values[y][x][d][0] - 1000 == maze_values[y][x][(d - 1) % 4][0]:
        tiles.append((x, y, (d - 1) % 4, score - 1000))
    if maze_values[y][x][d][0] - 1000 == maze_values[y][x][(d + 1) % 4][0]:
        tiles.append((x, y, (d + 1) % 4, score - 1000))
    tiles_.add((x, y))
print(len(tiles_))
