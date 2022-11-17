import sys

check = [False, False] + [True] * 10000

for i in range(2, 101):
    if check[i] == True:
        for j in range(i + i, 10001, i):
            check[j] = False

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    A = n // 2
    B = A
    for _ in range(10000):
        if check[A] and check[B]:
            print(A, B)
            break
        A -= 1
        B += 1 