import sys

N = int(sys.stdin.readline())
num = list()

for _ in range(N):
    a = int(sys.stdin.readline())
    num.append(a)

num.sort()
for i in num:
    print(i)
