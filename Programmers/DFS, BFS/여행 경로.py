def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def dfs(start, path):
        if len(tickets) + 1 == len(path):
            answer.append(path)
            return
        
        for i, ticket in enumerate(tickets):
            if ticket[0] == start and visited[i] == False:
                visited[i] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[i] = False
                
    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]