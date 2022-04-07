# time over

import sys

cnt_0 = 0
cnt_1 = 0

def fibonacci(n):
    global cnt_0
    global cnt_1
    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = sys.stdin.readline()

for _ in range(int(T)):
    n = sys.stdin.readline()
    fibonacci(int(n))

    print(cnt_0, cnt_1)
    cnt_0 = 0
    cnt_1 = 0    
