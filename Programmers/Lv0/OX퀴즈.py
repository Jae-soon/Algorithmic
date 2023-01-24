def solution(quiz):
    answer = []
    for i in quiz:
        q = i.split(" = ")
        ans = eval(q[0])

        if ans == int(q[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer