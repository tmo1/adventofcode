# https://adventofcode.com/2024/day/7#part2

def possible(subtotal, i): return True if i == len(numbers) and subtotal == value else False if subtotal > value or i == len(numbers) else possible(subtotal * numbers[i], i + 1) or possible(subtotal + numbers[i], i + 1) or possible(int(str(subtotal) + str(numbers[i])), i + 1)
total = 0
for line in open(0):
    value, numbers = int(line[:line.find(':')]), [int(n) for n in line[line.find(':') + 2:].split()]
    total += value if possible(numbers[0],1) else 0
print(total)
