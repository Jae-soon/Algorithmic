import sys

N = int(sys.stdin.readline())
num = [0] * 10001

for _ in range(N):
    a = int(sys.stdin.readline())
    num[a] = num[a] + 1

for i in range(10001):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)
