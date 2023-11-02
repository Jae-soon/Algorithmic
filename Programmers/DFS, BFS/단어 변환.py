visited = []
result = []

def solution(begin, target, words):
    answer = 0
    
    visited = [False] * len(words)
    
    if target not in words:
        return answer
    
    def dfs(word, depth):
        if word == target:
            result.append(depth)
            return
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            
            if differ(word, words[i]) == 1:
                visited[i] = True
                dfs(words[i], depth + 1)
                visited[i] = False
                
    dfs(begin, 0)
    
    answer = min(result)
    return answer

def differ(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    
    return count