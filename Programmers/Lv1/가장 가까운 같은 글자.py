def solution(s):
    answer = []
    sp = []

    for i, v in enumerate(s):
        if v in sp:
            answer.append(i - sp.index(v))
            sp[sp.index(v)] = "-1"
            sp.append(v)
        else:
            sp.append(v)
            answer.append(-1)
        

    return answer