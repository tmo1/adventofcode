# https://adventofcode.com/2017/day/14

key_string, total = open(0).readline().strip(), 0
for i in range(128):
    numbers, current, skip, lengths = [n for n in range(256)], 0, 0, [ord(x) for x in key_string + '-' + str(i)] + [
        17, 31, 73, 47, 23]
    for j in range(64):
        for length in lengths:
            x = current + length
            if x < 256:
                numbers = numbers[:current] + list(reversed(numbers[current:x])) + numbers[x:]
            else:
                x -= 256
                r = list(reversed(numbers[current:] + numbers[:x]))
                numbers = r[256 - current:] + numbers[x:current] + r[:256 - current]
            current = (current + length + skip) % 256
            skip += 1
    for j in range(0, 256, 16):
        x = 0
        for k in range(j, j + 16):
            x ^= numbers[k]

        total += len([1 for y in bin(x)[2:] if y == '1'])
print(total)
