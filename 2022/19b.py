# https://adventofcode.com/2022/day/19#part2
# based on 19a.py, which was based on a crucial insight I missed, found here:
# https://old.reddit.com/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j11kdm9/
# this takes 9m25s on my W550s for my input

import sys

blueprints = []
for line in sys.stdin:
    line = line.split()
    blueprints.append([[int(line[6]), 0, 0], [int(line[12]), 0, 0], [int(line[18]), int(line[21]), 0], [int(line[27]), 0, int(line[30])]])


def do_blueprint(minute, materials, robots, next_robot):
    global max_geodes
    if minute == 31:
        max_geodes = max(max_geodes, materials[3] + robots[3])
        return
    new_materials = [m for m in materials]
    new_minute = minute
    while new_materials[0] < blueprints[i][next_robot][0] or new_materials[1] < blueprints[i][next_robot][1] or new_materials[2] < blueprints[i][next_robot][2]:
        new_materials = [new_materials[j] + robots[j] for j in range(4)]
        new_minute += 1
        if new_minute == 31:
            do_blueprint(31, new_materials, robots, None)
            return
        if new_minute == 30 and next_robot < 3 or new_minute == 29 and next_robot < 2 or new_minute == 28 and next_robot == 0:
            return
    new_materials = [new_materials[j] + robots[j] for j in range(4)]
    for j in range(3):
        new_materials[j] -= blueprints[i][next_robot][j]
    new_robots = [r for r in robots]
    new_robots[next_robot] += 1
    for k in range(3, -1, -1):
        if k == 3 or new_robots[k] < max_robots[k]:
            do_blueprint(new_minute + 1, [nm for nm in new_materials], [nr for nr in new_robots], k)


total = 1
for i in range(3):
    max_geodes = 0
    max_robots = [max([blueprints[i][x][y] for x in range(4)]) for y in range(3)]
    for n in range(3, -1, -1):
        do_blueprint(0, [0, 0, 0, 0], [1, 0, 0, 0], n)
    total *= max_geodes
print(total)
