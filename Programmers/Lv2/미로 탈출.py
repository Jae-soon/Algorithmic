from collections import deque

def bfs(start, end, map):
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]

    n = len(map) # 세로 길이
    m = len(map[0]) # 가로 길이
    visited = [[False] * m for _ in range(n)]
    q = deque()
    flag = False

    # 초기값 셋팅
    for i in range(n):
        for j in range(m):
            if map[i][j] == start:
                q.append([i, j, 0]) # 시작점 좌표
                visited[i][j] == True
                flag = True
                break
        
        if flag:
            break

    while q:
        y, x, cost = q.popleft()
        
        # 종료지점 도착 시 이동 거리만큼 반환
        if map[y][x] == end:
            return cost
        
        # 상하좌우 이동
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 맵 밖 or 벽이 아닐 경우 이동
            if 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 'X':
                # 방문하지 않은 통로 체크
                if not visited[ny][nx]:
                    q.append([ny, nx, cost + 1])
                    visited[ny][nx] = True
    
    return -1

def solution(maps):
    p1 = bfs("S", "L", maps)
    p2 = bfs("L", "E", maps)
    
    if p1 != -1 and p2 != -1:
        return p1 + p2

    return -1