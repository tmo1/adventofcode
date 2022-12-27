# https://adventofcode.com/2022/day/25

import sys; s, c = [], 0
d, dr = {'2':2,'1':1,'0':0,'-':-1,'=':-2}, {2:'2',1:'1',0:'0',3:'=',4:'-',5:'0'}
n = sum([sum((5 ** i) * d[x] for i, x in enumerate(reversed(l.strip()))) for l in sys.stdin])
while n > 0:
    x = n % 5 + c; s.append(dr[x]); c = 1 if x > 2 else 0; n //= 5
print(''.join(reversed(s)))
