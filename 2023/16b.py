# https://adventofcode.com/2023/day/16#part2

optics = [line.strip() for line in open(0)]
physics = {0: {'dx': 0, 'dy': -1, '/': [2], '\\': [1], '-': [1, 2]}, 1: {'dx': -1, 'dy': 0, '/': [3], '\\': [0], '|': [0, 3]}, 2: {'dx': 1, 'dy': 0, '/': [0], '\\': [3], '|': [0, 3]}, 3: {'dx': 0, 'dy': 1, '/': [1], '\\': [2], '-': [1, 2]}}
max_energized = 0
for direction in range(4):
    for i in range(len(optics)):
        photons = [[-1 if direction == 2 else len(optics) if direction == 1 else 0, -1 if direction == 3 else len(optics) if direction == 0 else 0, direction]]
        photons[0][0], photons[0][1] = i if direction in {0, 3} else photons[0][0], i if direction in {1, 2} else photons[0][1]
        energized = [[[False for i in range(4)] for x in range(len(optics))] for y in range(len(optics))]
        while photons:
            photon = photons.pop()
            photon[0], photon[1] = photon[0] + physics[photon[2]]['dx'], photon[1] + physics[photon[2]]['dy']
            if 0 <= photon[0] < len(optics) and 0 <= photon[1] < len(optics):
                new_directions = physics[photon[2]][optics[photon[1]][photon[0]]] if optics[photon[1]][photon[0]] in physics[photon[2]] else [photon[2]]
                for new_d in new_directions:
                    if not energized[photon[1]][photon[0]][new_d]:
                        photons.append([photon[0], photon[1], new_d])
                        energized[photon[1]][photon[0]][new_d] = True
        max_energized = max(max_energized, sum([1 for row in energized for cell in row if True in cell]))
print(max_energized)
