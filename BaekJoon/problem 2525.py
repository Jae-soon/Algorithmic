h, m = map(int, input().split())
time = int(input())

if m + time >= 60:
    h = int(h + (m + time) / 60)
    if h >= 24:
        h = h - 24
    print(h, ((m + time) % 60))
else:
    print(h, m + time)