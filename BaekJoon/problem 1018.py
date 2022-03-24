'''
google 도움 받음, 조금 더 이해 필요
'''

N, M = map(int, input().split())
board = list()

for _ in range(N):
    board.append(input())

repair = list()

# 8 x 8 크기로 자르기(ex. 10 x 10일 경우 3*3 가지의 방법)
for i in range(N - 7):
    for j in range(M - 7):
        f_W = 0
        f_B = 0
        
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                # 휜색 or 검은색일 경우의 확률(1/2)
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        f_W += 1
                    if board[k][l] != 'B':
                        f_B += 1
                else:
                    if board[k][l] != 'W':
                        f_B += 1
                    if board[k][l] != 'B':
                        f_W += 1
        repair.append(f_W)
        repair.append(f_B)
print(min(repair))