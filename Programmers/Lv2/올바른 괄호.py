from collections import deque

def solution(s):
    answer = True
    
    dq = deque()
    dq2 = deque()

    for i in s:
        dq.append(i)

    if s[0] == ")":
        return False

    while dq:
        a = dq.popleft()
        if a == "(":
            dq2.append(a)
        
        else:
            if not dq2:
                return False
            dq2.popleft()
    
    if dq2:
        return False
 
    return True