# 정규식사용

import sys
import re

inf = sys.stdin
t = inf.readline()

for _ in range(int(t)):
    a = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(a)
    if m:
        print("YES")
    else:
        print("NO")
