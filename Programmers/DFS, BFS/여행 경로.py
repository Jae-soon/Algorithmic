from collections import deque, defaultdict

answer = []
graph = defaultdict(list)

def dfs(s):
    # print(graph[s])
    while graph[s]:
        dfs(graph[s].pop(0))
    print(s)
    if not graph[s]:
        answer.append(s)
        # print(graph)
        # print(answer)
        return

def solution(tickets):

    for start, end in tickets:
        graph[start].append(end)
    
    print(graph)

    for a, b in graph.items():
        graph[a].sort()

    print(graph)

    dfs("ICN")

    return answer[::-1]

# def dfs(i, tickets, search):    
#     answer = []
#     start = "ICN"
#     dq = deque()

#     [start, end] = dq.popleft()
#     if False not in search:
#         return answer

#     if tickets[i][0] == end and not search:
#         answer.append(start)
#         dq.append(tickets[i])
#         search[i] = True
    
#     dfs(i + 1, tickets, search)


# def solution(tickets):
#     answer = []
    
#     search = [False] * len(tickets)

#     dfs(0, tickets, search)
#     return answer