import sys

inf = sys.stdin
T = inf.readline()

for _ in range(int(T)):
    x1, y1, x2, y2 = map(int, inf.readline().split())
    n = int(inf.readline())
    count = 0
    st = 0
    for _ in range(n):
        cx, cy, r = map(int, inf.readline().split())
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        cr = r**2

        if cr > dis1 and cr > dis2:
            pass
        elif cr > dis1:
            count += 1
        elif cr > dis2:
            count += 1
    
    print(count)