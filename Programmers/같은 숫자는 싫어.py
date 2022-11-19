from collections import deque

def solution(arr):
    answer = []
    q = deque()
    for i in arr:
        q.append(i)
    
    for _ in range(len(arr)):
        a = q.popleft()
        
        if a not in answer:
            answer.append(a)
        
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))
