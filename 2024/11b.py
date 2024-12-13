# https://adventofcode.com/2024/day/11#part2
# Same solution as part 1, just with the 'for' loop to 75 as opposed to 25

from collections import defaultdict
stones = defaultdict(lambda : 0)
for stone in open(0).read().split(): stones[stone] += 1
for i in range(75):
    new_stones = defaultdict(lambda : 0)
    for k, v in stones.items():
        if k == '0': new_stones['1'] += v
        elif len(k) % 2 == 0:
            new_stones[k[:len(k) // 2]] += v
            new_stones[str(int(k[len(k) // 2:]))] += v
        else: new_stones[str(int(k) * 2024)] += v
    stones = new_stones
print(sum(stones.values()))
