import sys

inf = sys.stdin
N = inf.readline()

li = list()

for _ in range(int(N)):
    li.append(input().split())

li.sort(key=lambda x: x[0])

for i in li:
    print(i[0], i[1])