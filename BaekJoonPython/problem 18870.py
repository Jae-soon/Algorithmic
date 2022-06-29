import sys

inf = sys.stdin
n = inf.readline()
x = list(map(int, input().split()))

sort_x = sorted(list(set(x)))
dic = {sort_x[i]: i for i in range(len(sort_x))}
for i in x:
    print(dic[i], end = ' ')