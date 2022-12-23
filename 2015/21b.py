# https://adventofcode.com/2015/day/21#part2

import sys
boss_stats = []
for line in sys.stdin:
    words = line.split()
    boss_stats.append(int(words[-1]))


def fight(player, boss):
    while True:
        boss[0] -= (player[1] - boss[2])
        if boss[0] <= 0:
            return True
        player[0] -= (boss[1] - player[2])
        if player[0] <= 0:
            return False


gold = 357
weapons = {8: 4, 10: 5, 25: 6, 40: 7, 74: 8}
armor = {13: 1, 31: 2, 53: 3, 75: 4, 102: 5, 0: 0}
rings = {25: (1, 0), 50: (2, 0), 100: (3, 0), 20: (0, 1), 40: (0, 2), 80: (0, 3), 0: (0, 0)}
while True:
    gold -= 1
    for weapon in weapons.keys():
        for arm in armor.keys():
            cost1 = weapon + arm
            if cost1 > gold:
                continue
            for ring1 in rings.keys():
                cost2 = cost1 + ring1
                if cost2 > gold:
                    continue
                for ring2 in rings.keys():
                    if ring2 == ring1 and ring2 != 0:
                        continue
                    cost3 = cost2 + ring2
                    if cost3 == gold and not fight([100, weapons[weapon] + rings[ring1][0] + rings[ring2][0], armor[arm] + rings[ring1][1] + rings[ring2][1]], boss_stats[:]):
                        print(cost3)
                        exit()
