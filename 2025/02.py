# https://adventofcode.com/2025/day/2

invalid = 0
for product_range in open(0).readline().split(','):
    lower, upper = [int(n) for n in product_range.split('-')]
    for i in range(lower, upper + 1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]: invalid += i
print(invalid)