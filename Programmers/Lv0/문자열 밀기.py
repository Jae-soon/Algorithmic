def solution(A, B):
    answer = 0
    count = 0
    q = list()

    for i in A:
        q.append(i)

    while 1:
        q_str = "".join(q)
        if answer == len(B):
            return -1
        if q_str == B:
            break
        last_str = q.pop()
        q.insert(0, last_str)
        answer += 1

    return answer