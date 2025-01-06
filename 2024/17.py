# https://adventofcode.com/2024/day/17

import re

numbers, output, i = [int(n) for n in re.findall(r"\d+", open(0).read())], [], 3
while i < len(numbers):
    match numbers[i]:
        case 0: numbers[0] //= 2 ** (numbers[i + 1] if numbers[i + 1] <= 3 else numbers[numbers[i + 1] - 4])
        case 1: numbers[1] ^= numbers[i + 1]
        case 2: numbers[1] = (numbers[i + 1] if numbers[i + 1] <= 3 else numbers[numbers[i + 1] - 4]) % 8
        case 3: i = numbers[i + 1] + 1 if numbers[0] != 0 else i
        case 4: numbers[1] ^= numbers[2]
        case 5: output.append(str((numbers[i + 1] if numbers[i + 1] <= 3 else numbers[numbers[i + 1] - 4]) % 8))
        case 6: numbers[1] = numbers[0] // 2 ** (numbers[i + 1] if numbers[i + 1] <= 3 else numbers[numbers[i + 1] - 4])
        case 7: numbers[2] = numbers[0] // 2 ** (numbers[i + 1] if numbers[i + 1] <= 3 else numbers[numbers[i + 1] - 4])
    i += 2
print(','.join(output))
