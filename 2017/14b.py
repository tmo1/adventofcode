# https://adventofcode.com/2017/day/14#part2
# This takes about 45 seconds for my input on my W550s

key_string, regions = open(0).readline().strip(), []
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
    hex_digits = []
    for j in range(0, 256, 16):
        x = 0
        for k in range(j, j + 16):
            x ^= numbers[k]
        hex_digits += list(format(x, '02x'))
    binary_digits = []
    for x in hex_digits:
        binary_digits += format(int(x, 16), '04b')
    for c, x in enumerate(binary_digits):
        if x == '1':
            regions.append({(c, i)})


def combine_regions(r1, r2):
    for square1 in r1:
        for square2 in r2:
            if (square1[0] == square2[0] and abs(square1[1] - square2[1]) == 1) or (square1[1] == square2[1] and abs(square1[0] - square2[0]) == 1):
                return True
    return False


done = False
while not done:
    new_regions, combined, done = [], set(), True
    for i, region1 in enumerate(regions):
        if i not in combined:
            for j, region2 in enumerate(regions[i + 1:], i + 1):
                if len(region1 & region2) > 0:
                    print('error!', i, region1, j, region2)
                    quit()
                if j not in combined and combine_regions(region1, region2):
                    new_regions.append(region1 | region2)
                    combined |= {i, j}
                    done = False
                    break
            if i not in combined:
                new_regions.append(region1)
    regions = new_regions
print(len(regions))
