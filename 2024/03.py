# https://adventofcode.com/2024/day/3

import re

print(sum([int(match[0]) * int(match[1]) for match in re.findall(r"mul\((\d+),(\d+)\)", open(0).read())]))
