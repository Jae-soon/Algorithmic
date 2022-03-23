N = int(input())
dc_list = list()

for _ in range(N):
    x, y = map(int, input().split())
    dc_list.append((x, y))

for i in dc_list:
    cnt = 1
    for j in dc_list:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=" ")