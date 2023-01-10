# https://adventofcode.com/2016/day/11
# Dijkstra's algorithm implemented via a priority queue
# takes 10.263s for the first part (with the 'elerium' / 'dilithium' line commented out) for my input on my W550s,
# and 11m54.972s for the second part on my Z440

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


floors, states = [set() for i in range(4)], {}
for count, line in enumerate(sys.stdin):
    line = line.split()
    i = 0
    if line[4] == 'nothing':
        continue
    while line[i] != 'a':
        i += 1
    while i < len(line):
        if line[i] == 'and':
            i += 1
        if line[i + 2][:3] == 'mic':
            material = line[i + 1][:-11]
            floors[count].add((material, 'm'))
        else:
            material = line[i + 1]
            floors[count].add((material, 'g'))
        i += 3
# comment out the following line for part 1, leave it uncommented for part 2
floors[0] |= {('elerium', 'm'), ('elerium', 'g'), ('dilithium', 'm'), ('dilithium', 'g')}
total = len([item for x in floors for item in x])
visited = set()


def safe(f, first_floor):
    for j in [first_floor, first_floor + 1]:
        for item in f[j]:
            if item[1] == 'm' and (item[0], 'g') not in f[j] and sum([1 for x in f[j] if x[1] == 'g']) > 0:
                return False
    return True


current = tuple([tuple(sorted(x)) for x in floors] + [0])
add_task(current, 0)
last_min = 0
turns = 0
while len(current[3]) != total:
    elevator = current[4]
    new_turns = turns + 1
    no_down = True if (elevator == 0) or (
                len(current[0]) == 0 and (elevator == 1 or (len(current[1]) == 0 and elevator == 2))) else False
    floors = [{x for x in current[i]} for i in range(4)]
    for item1 in current[elevator]:
        for item2 in current[elevator]:
            cargo = {item1, item2}
            floors[elevator] -= cargo
            if elevator < 3:
                floors[elevator + 1] |= cargo
                new_state = tuple([tuple(sorted(x)) for x in floors] + [elevator + 1])
                if safe(new_state, elevator) and new_state not in visited and (
                        new_state not in entry_finder or entry_finder[new_state][0] > new_turns):
                    add_task(new_state, new_turns)
                floors[elevator + 1] -= cargo
            if no_down is False:
                floors[elevator - 1] |= cargo
                new_state = tuple([tuple(sorted(x)) for x in floors] + [elevator - 1])
                if safe(new_state, elevator - 1) and new_state not in visited and (
                        new_state not in entry_finder or entry_finder[new_state][0] > new_turns):
                    add_task(new_state, new_turns)
                floors[elevator - 1] -= cargo
            floors[elevator] |= cargo
    visited.add(current)
    current, turns = pop_task()
print(turns)
