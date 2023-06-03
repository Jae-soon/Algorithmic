from collections import deque

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)] # 모든 연결된 노드의 경우의 수

# 양방향으로 연결되어 있는 노드값을 True로 변경
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

def bfs(v):
    q = deque([v])
    visited1[v] = True

    while q:
        v = q.popleft() # 인접한 노드를 순서대로 넣은 후 하나하나씩 빼내는 방법
        print(v, end=" ")
        for i in range(1, n + 1):
            if not visited1[i] and graph[v][i]: # 인접하고, 중복되지 않는 숫자 대입
                q.append(i)
                visited1[i] = True

def dfs(v):
    visited2[v] = True
    print(v, end=" ")
    for i in range(1, n + 1):
        if not visited2[i] and graph[v][i]:
            dfs(i)

dfs(v)
print()
bfs(v)
