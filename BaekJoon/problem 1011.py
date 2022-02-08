import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int, input().split())
    dis = y - x
    cnt = 0
    move = 1
    move_plus = 0
    while move_plus < dis:
        cnt += 1
        move_plus += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)