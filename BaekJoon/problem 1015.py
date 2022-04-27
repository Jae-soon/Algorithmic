import sys

inf = sys.stdin
n = int(inf.readline())

a = list(map(int, input().split()))
b = [0] * n
sort_a = sorted(a)
count = 0

for i in sort_a:
    index = a.index(i)
    a[index] = -1
    b[index] = count
    count += 1

for i in b:
    print(i, end = " ")