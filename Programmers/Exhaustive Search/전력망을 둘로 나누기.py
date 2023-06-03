from collections import deque

n = 0
def bfs(node, graph, visited, wire, cnt):
    queue = deque([node, graph, visited, wire])
    visited[node] = True

    while queue:
        node, graph, visited, wire = queue.popleft()
        cnt += 1

        for i in range(1, n + 1):
            if not (graph[]) or (node == wire[1] and i == wire[0])):
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, graph, visited, wire])

    return cnt


def solution(n, wires):
    answer = 1e9
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for wire in wires:
        [a, b] = wire
        graph[a][b] = True
        graph[b][a] = True

    for wire in wires:
        visited = [False] * (n + 1)
        temp = []

        graph[wire[0]][wire[1]] = False
        graph[wire[1]][wire[0]] = False

        for i in range(1, n + 1):
            if not visited[i]:
                cnt = bfs(i, graph, visited, wire, 0)

    # for wire in wires:
    #     visited = [False] * (n + 1)
    #     temp = []
    #     for i in range(1, n + 1):
    #         if not visited[i]:
    #             cnt = bfs(i, graph, visited, wire, 0)
    #             temp.append(cnt)

    #     answer = min(answer, abs(temp[0] - temp[1]))

    return answer