# https://adventofcode.com/2016/day/14#part2
# takes  33.141s for my input on my W550s

import sys
import hashlib

salt, n, triplets, otp_keys = sys.stdin.readline().strip(), 0, {}, set()
while True:
    h = hashlib.md5((salt + str(n)).encode()).hexdigest()
    for i in range(2016):
        h = hashlib.md5(h.encode()).hexdigest()
    triplets = {k: v for k, v in triplets.items() if n - k < 1001}
    for i in range(4, len(h)):
        if h[i - 4] == h[i - 3] == h[i - 2] == h[i - 1] == h[i]:
            new_triplets = {}
            for j, t in triplets.items():
                if t == h[i]:
                    otp_keys.add(j)
                else:
                    new_triplets[j] = t
            triplets = new_triplets
    if len(otp_keys) >= 64:
        if len(triplets) == 0:
            print(sorted(otp_keys)[63])
            quit()
    else:
        for i in range(2, len(h)):
            if h[i - 2] == h[i - 1] == h[i]:
                triplets[n] = h[i]
                break
    n += 1
