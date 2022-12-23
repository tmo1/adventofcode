# https://adventofcode.com/2022/day/4

import sys
import re

pairs = 0
for line in sys.stdin:
    first = line
    nums = [int(x) for x in re.split(r'[,-]', line)]
    if (nums[2] >= nums[0] and nums[3] <= nums[1]) or (nums[0] >= nums[2] and nums[1] <= nums[3]):
        pairs += 1
print(pairs)
