# https://adventofcode.com/2023/day/6#part2
# The original version of this solution worked for the example and my input, but is incorrect for cases of tied races.
# See: https://old.reddit.com/r/adventofcode/comments/18bwe6t/2023_day_6_solutions/kca9sfd/

from math import sqrt, ceil

race_time, race_distance = [int(''.join([n for n in line.split()[1:]])) for line in open(0)]
discriminant = sqrt(race_time ** 2 - (4 * race_distance))
#print(int((race_time + discriminant) / 2) - ceil((race_time - discriminant) / 2) + 1)
print(ceil((race_time + discriminant) / 2) - 1 - int((race_time - discriminant) / 2))
