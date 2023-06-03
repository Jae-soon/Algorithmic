import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque()
    
    for i, v in enumerate(progresses):
        dq.append(math.ceil((100 - v) / speeds[i]))
    
    count = 1
    while dq:
        deploy_time = dq.popleft()
        if not dq:
            answer.append(count)
            break
        
        diff = dq.popleft()
        if diff > deploy_time:
            answer.append(count)
            dq.appendleft(diff)
            count = 1
        else:
            count += 1
            dq.appendleft(deploy_time)

            
            
    return answer