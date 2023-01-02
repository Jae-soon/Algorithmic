from collections import deque

def solution(maps):
    def dfs(x, y):
        dq = deque()
        dq.append([x, y, 1])

        while dq:
            [y, x, distance] = dq.popleft()

            if y == len(maps) - 1 and x == len(maps[0]) - 1: # 끝일 경우 return
                return distance
            
            if maps[y][x] == 0: # 막힌 곳이라면 패스
                continue
            
            maps[y][x] = 0 # 지나간 곳은 0으로 치환.

            if y + 1 < len(maps): # 위쪽으로 갔을 경우
                dq.append([y + 1, x, distance + 1])
            if y - 1 >= 0: # 아래쪽으로 갔을 경우
                dq.append([y - 1, x, distance + 1])
            if x - 1 >= 0: # 왼쪽으로 갔을 경우
                dq.append([y, x - 1, distance + 1])
            if x + 1 < len(maps[0]): # 오른쪽으로 갔을 경우
                dq.append([y, x + 1, distance + 1])
            

        return -1
                        
    return dfs(0, 0)
