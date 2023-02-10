from collections import deque

def solution(priorities, location):
    dq = deque()
    dq2 = deque()
    for i, k in enumerate(priorities):
        dq.append([i, k])
    
    while dq:
        [index, diff] = dq.popleft() # 0, 2
        dq2.append(index)
        if dq: # 첫 popleft를 해주었을 때 dq가 있을 경우
            for i in dq:
                if i[1] > diff: # 뒤로가는 경우
                    dq.append([index, diff])
                    dq2.pop()
                    break
                
    return dq2.index(location) + 1
