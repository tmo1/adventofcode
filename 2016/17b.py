# https://adventofcode.com/2016/day/17#part2

import sys
import hashlib


def add_path_location(new_path, new_location):
    global longest
    if new_location[0] == new_location[1] == 3:
        longest = max(longest, len(new_path))
        return
    new_paths[new_path] = new_location


passcode, paths, open_letters, longest = list(sys.stdin.readline().strip()), {(): (0, 0)}, {'b', 'c', 'd', 'e', 'f'}, 0
while paths:
    new_paths = {}
    for path, location in paths.items():
        h = hashlib.md5(''.join(passcode + list(path)).encode()).hexdigest()
        if h[0] in open_letters and location[1] != 0:
            add_path_location(tuple(list(path) + ['U']), (location[0], location[1] - 1))
        if h[1] in open_letters and location[1] != 3:
            add_path_location(tuple(list(path) + ['D']), (location[0], location[1] + 1))
        if h[2] in open_letters and location[0] != 0:
            add_path_location(tuple(list(path) + ['L']), (location[0] - 1, location[1]))
        if h[3] in open_letters and location[0] != 3:
            add_path_location(tuple(list(path) + ['R']), (location[0] + 1, location[1]))
    paths = new_paths
print(longest)
