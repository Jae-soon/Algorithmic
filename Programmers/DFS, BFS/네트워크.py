def dfs(n, computers, computer, visit):
    visit[computer] = True
    for con in range(n):
        if con != n and computers[computer][con] == 1:
            if visit[con] == False:
                dfs(n, computers, con, visit)

def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]

    for computer in range(n):
        if visit[computer] == False:
            dfs(n, computers, computer, visit)
            answer += 1

    return answer