# https://adventofcode.com/2022/day/19
# a much more efficient solution than 19.py, based on this crucial insight that I missed:
# "I don’t build robots I don’t need. e.g. if the geode robots cost x obsidian I will never build more than x obsidian miners."
# https://old.reddit.com/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j11kdm9/

import sys

blueprints = []
for line in sys.stdin:
    line = line.split()
    blueprints.append([[int(line[6]), 0, 0], [int(line[12]), 0, 0], [int(line[18]), int(line[21]), 0], [int(line[27]), 0, int(line[30])]])


def do_blueprint(minute, materials, robots, next_robot):
    global max_geodes
    if minute == 23:
        max_geodes = max(max_geodes, materials[3] + robots[3])
        return
    new_materials = [m for m in materials]
    new_minute = minute
    while new_materials[0] < blueprints[i][next_robot][0] or new_materials[1] < blueprints[i][next_robot][1] or new_materials[2] < blueprints[i][next_robot][2]:
        new_materials = [new_materials[j] + robots[j] for j in range(4)]
        new_minute += 1
        if new_minute == 23:
            do_blueprint(23, new_materials, robots, None)
            return
    new_materials = [new_materials[j] + robots[j] for j in range(4)]
    for j in range(3):
        new_materials[j] -= blueprints[i][next_robot][j]
    new_robots = [r for r in robots]
    new_robots[next_robot] += 1
    for k in range(4):
        if k == 3 or new_robots[k] < max([blueprints[i][z][k] for z in range(k, 4)]):
            do_blueprint(new_minute + 1, [nm for nm in new_materials], [nr for nr in new_robots], k)


total_quality = 0
for i in range(len(blueprints)):
    max_geodes = 0
    for n in range(4):
        do_blueprint(0, [0, 0, 0, 0], [1, 0, 0, 0], n)
    total_quality += (i + 1) * max_geodes
print(total_quality)
