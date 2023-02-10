from collections import deque

def bfs(map, s, d, point):
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    x, y = s
    q = deque()
    q.append([x, y, point])

    while q:
        x, y, point = q.popleft()
        for dx, dy in move:
            mx, my = x + dx, y + dy
            if mx == d[0] and my == d[1]:
                return point + 1
            elif 0 <= mx < len(map) and 0 <= my < len(map[0]) and map[mx][my] == 0:
                map[mx][my] = 0
                q.append([mx, my, point + 1])
    return -1

def solution(M, S, D):
    answer = 0
    answer = bfs(M, S, D, 0)
    return answer
        