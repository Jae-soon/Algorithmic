# 시간초과 발생

A, B, C = list(map(int, input().split()))
count = 1

while True:
    C = C - A
    if C <= 0:
        print(count)
        break
    C = C + B
    count = count + 1