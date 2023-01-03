from collections import deque

def dfs(i, tickets, search):    
    answer = []
    start = "ICN"
    dq = deque()

    [start, end] = dq.popleft()
    if False not in search:
        return answer

    if tickets[i][0] == end and not search:
        answer.append(start)
        dq.append(tickets[i])
        search[i] = True
    
    dfs(i + 1, tickets, search)


def solution(tickets):
    answer = []
    
    search = [False] * len(tickets)

    dfs(0, tickets, search)
    return answer