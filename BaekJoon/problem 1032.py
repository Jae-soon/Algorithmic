import sys

inf = sys.stdin
n = inf.readline()
a = list(input())
a_len = len(a)

for _ in range(int(n) - 1):
    b = list(input())
    for i in range(a_len):
        if a[i] != b[i]:
            a[i] = '?'

print(''.join(a))