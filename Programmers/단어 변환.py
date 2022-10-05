from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0]) # words의 단어와 index queue에 넣기
    v = [0 for _ in range(len(words))]

    while q:
        word, index = q.popleft() # queue의 첫번째 값
        
        if word == target:
            answer = index
            break
        
        for i in range(len(words)): # 0 1 2 3 4 5 
            diff = 0
            if not v[i]: # v[i] = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff += 1
                
                if diff == 1:
                    q.append([words[i], index + 1])
                    v[i] = 1
    
    return answer