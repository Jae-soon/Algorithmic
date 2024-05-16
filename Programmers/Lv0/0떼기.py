from collections import deque

def solution(n_str):
    answer = ''
    
    li = list(n_str)
    idx = 0

    for i in li:
        if i != "0":
            idx = li.index(i)
            break
        
    answer = ''.join(li[idx:])
    return answer