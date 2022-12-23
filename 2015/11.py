# https://adventofcode.com/2015/day/11

import sys
password = sys.stdin.readline().strip()
password = [ord(c) for c in password]


def increment(position):
    if password[position] == 122:
        password[position] = 97
        increment(position - 1)
    elif password[position] in {104, 107, 110}:
        password[position] += 2
    else:
        password[position] += 1


while set(password) & {105, 108, 111}:
    increment(len(password) - 1)

while True:
    increment(len(password) - 1)
    rule1 = rule2 = flag1 = False
    n = 100
    for i in range(1, len(password)):
        if password[i] - password[i - 1] == 1:
            if flag1:
                rule1 = True
            else:
                flag1 = True
        else:
            flag1 = False
        if password[i] == password[i - 1]:
            if n < i - 2:
                rule2 = True
            else:
                n = i - 1
    if rule1 and rule2:
        for c in password:
            print(chr(c), end='')
        print()
        break
