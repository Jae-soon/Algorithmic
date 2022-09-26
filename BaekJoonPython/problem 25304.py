import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
total = 0

for _ in range(n):
    a, b = map(int, input().split())

    total = total + (a * b)

if(total == x):
    print("Yes")
else:
    print("No")