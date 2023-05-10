from collections import deque

def solution(n, m, section):
    answer = 1
    
    dq = deque(section)
    standard = dq[0] + m - 1
    
    while dq:
        if dq[0] <= standard:
            dq.popleft()
        else:
            answer += 1
            standard = dq[0] + m - 1
        
    return answer