# retry

from collections import deque

def solution(board):
    dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x, y):
        dq = deque()
        dq.append((x, y))
        while dq:
            a, b = dq.popleft()
            visited[a][b] = True
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                #위험지역으로 둬야함 
                if 0<=nx<length and 0<=ny<length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        dq.append((nx, ny))
                    else:
                        board[nx][ny] = 2 #위험지역 처리 

    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i, j)
    result = 0
    for i in range(length):
        result += board[i].count(0)
    return result
# def solution(board):
#     answer = 0

#     for x in range(len(board)):
#         for y in range(len(board)):
#             if board[x][y] == 1:
#                 if x == 0:
#                     if y == 0:
                        
#                 for i in range(-1, 2):
#                     if board[x + i][y + i] == 1 or not board[x + i][y + i]:
#                         pass
#                     else:
#                         board[x + i][y + i] == 2
    
#     print(board)
        
            
#     return answer