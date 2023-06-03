from collections import deque
def solution(k, dungeons):
    answer = 0
    dq = deque()
    dq.append([k, []])

    while dq:
        fatigue, search = dq.popleft()
        for i in range(len(dungeons)):
            [a, b] = dungeons[i]
            if i not in search and fatigue >= a and fatigue - b >= 1:
                dq.append([fatigue - b, search + [i]])
            else:
                answer = max(answer, len(search))

        print(dq, answer)


    return answer