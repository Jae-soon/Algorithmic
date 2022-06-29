import sys

g = list()
zero = list()

for i in range(9):
    g.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
for i in range(9):
    for j in range(9):
        if g[i][j] == 0:
            zero.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == g[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == g[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == g[nx + i][ny + j]:
                return False
    return True

def dfs(idx):
    if idx == len(zero):
        for i in range(9):
            print(*g[i])
        exit(0)
    
    for i in range(1, 10):
        x = zero[idx][0]
        y = zero[idx][1]
        
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            g[x][y] = i
            dfs(idx + 1)
            g[x][y] = 0

dfs(0)