from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root]) # 1부터 시작

    while queue:
        n = queue.popleft() # 큐의 왼쪽부터 하나씩 출력
        if n not in visited:
            visited.append(n) # 도착 지점
            queue += graph[n] - set(visited) # 해당 지점의 값에서 이미 왔다 간 곳은 제외
    return visited

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
  
print(BFS_with_adj_list(graph_list, root_node))