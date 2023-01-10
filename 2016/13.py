# https://adventofcode.com/2016/day/13

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


visited, num = set(), int(sys.stdin.readline())
current, turns = (1, 1), 0
while current != (31, 39):
    new_turns = turns + 1
    for new_location in [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] - 1), (current[0], current[1] + 1)]:
        if new_location[0] > -1 and new_location[1] > -1 and new_location not in visited:
            if bin((new_location[0] + 3) * new_location[0] + ((new_location[1] + 1) * new_location[1]) + (2 * new_location[0] * new_location[1]) + num)[2:].count('1') % 2 == 1:
                visited.add(new_location)
                continue
            if new_location not in entry_finder or entry_finder[new_location][0] > new_turns:
                add_task(new_location, new_turns)
    visited.add(current)
    current, turns = pop_task()
print(turns)
