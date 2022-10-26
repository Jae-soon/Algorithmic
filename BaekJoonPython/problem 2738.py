import sys

a, b = [], []
n, m = map(int, sys.stdin.readline().split(" "))

for _ in range(n):
    a_row = list(map(int, sys.stdin.readline().split(" ")))
    a.append(a_row)

for _ in range(n):
    b_row = list(map(int, sys.stdin.readline().split(" ")))
    b.append(b_row)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end = " ")
    print()
