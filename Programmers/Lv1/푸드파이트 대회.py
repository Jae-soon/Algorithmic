from collections import deque

def solution(food):
    answer = ''
    dq = deque()
    dq.append("0")
    for i in range(len(food) - 1, 0, -1):
        for _ in range(food[i] // 2):
            dq.appendleft(str(i))
            dq.append(str(i))
    answer = "".join(dq)
    return answer