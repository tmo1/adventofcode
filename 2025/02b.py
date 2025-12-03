# https://adventofcode.com/2025/day/2#part2

invalid = 0
for product_range in open(0).readline().split(','):
    lower, upper = [int(n) for n in product_range.split('-')]
    for i in range(max(lower, 10), upper + 1):
        s = str(i)
        len_s = len(s)
        for j in (k for k in range(1, int(len_s ** .5) + 1) if len_s % k == 0):
            if s[:j] * (len_s // j) == s or (j != 1 and s[:len_s // j] * j == s):
                invalid += i
                break
print(invalid)