# https://adventofcode.com/2016/day/22#part2

import sys

# from https://docs.python.org/3/library/heapq.html

from heapq import heappush, heappop
import itertools

pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    """Add a new task or update the priority of an existing task"""
    if task in entry_finder:
        remove_task(task)
    c = next(counter)
    entry = [priority, c, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    """Mark an existing task as REMOVED.  Raise KeyError if not found."""
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    """Remove and return the lowest priority task. Raise KeyError if empty."""
    # modified from the documentation to return the priority of the popped task along with the task itself
    while pq:
        priority, c, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task, priority
    raise KeyError('pop from an empty priority queue')


sys.stdin.readline()
sys.stdin.readline()
xnodes, max_used, min_size = set(), 0, 1000000
for line in sys.stdin:
    line = line.split()
    size, used = int(line[1][:-1]), int(line[2][:-1])
    node = line[0].split('-')
    node_x, node_y = int(node[1][1:]), int(node[2][1:])
    if used <= min_size and size >= max_used:
        max_used = max(max_used, used)
        min_size = min(min_size, size)
        xnodes.add((node_x, node_y))
        if used == 0:
            zero_node = (node_x, node_y)
data_node = (max([x[0] for x in xnodes]), 0)
current, turns, visited = (zero_node[0], zero_node[1], data_node[0], data_node[1]), 0, set()
while current[2] != 0 or current[3] != 0:
    next_turns = turns + 1
    for new_zero in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1),
                     (current[0], current[1] - 1)]:
        if new_zero in xnodes:
            new_state = (new_zero[0], new_zero[1], current[2], current[3]) if new_zero[0] != current[2] or new_zero[
                1] != current[3] else (new_zero[0], new_zero[1], current[0], current[1])
            if new_state not in visited and (new_state not in entry_finder or entry_finder[new_state][0] > next_turns):
                add_task(new_state, next_turns)
    visited.add(current)
    current, turns = pop_task()
print(turns)
