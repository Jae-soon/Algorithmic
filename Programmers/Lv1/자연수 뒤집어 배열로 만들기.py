def solution(n):
    answer = []

    list_n = list(str(n))
    list_n.reverse()

    for i in list_n:
        answer.append(int(i))

    return answer