# https://adventofcode.com/2016/day/24#part2

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


ducts, pois, poi_distances, shortest = [], {}, {}, 1000000
for y, line in enumerate(sys.stdin):
    duct = []
    for x, char in enumerate(line.strip()):
        if char == '#':
            duct.append(char)
        else:
            duct.append('.')
            if char.isdigit():
                pois[char] = (x, y)
    ducts.append(duct)


def next_poi(prev_poi, remaining_pois, distance):
    global shortest, pq, entry_finder
    for poi in remaining_pois:
        if (prev_poi, poi) not in poi_distances:
            pq, entry_finder, current, current_distance, visited = [], {}, pois[prev_poi], 0, set()
            add_task(current)
            while current != pois[poi]:
                next_distance = current_distance + 1
                for neighbor in [(current[0] + 1, current[1]), (current[0] - 1, current[1]),
                                 (current[0], current[1] + 1), (current[0], current[1] - 1)]:
                    if ducts[neighbor[1]][neighbor[0]] == '.' and (
                            neighbor not in entry_finder or entry_finder[neighbor][0] >= next_distance):
                        add_task(neighbor, next_distance)
                visited.add(current)
                current, current_distance = pop_task()
            poi_distances[(prev_poi, poi)] = poi_distances[(poi, prev_poi)] = current_distance
        n = distance + poi_distances[(prev_poi, poi)]
        if n > shortest:
            return
        if len(remaining_pois) == 1:
            if '0' in remaining_pois:
                shortest = min(shortest, n)
                return
            next_poi(poi, {'0'}, n)
        else:
            next_poi(poi, remaining_pois - {poi}, n)


next_poi('0', {poi for poi in pois.keys() if poi != '0'}, 0)
print(shortest)
