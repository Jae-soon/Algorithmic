def solution(participant, completion):
    answer = ''
    if set(participant) != set(completion):
        a = list(set(participant) - set(completion))
        answer = a[0]
    else:
        dic_p = {}
        for data in participant:
            if data in dic_p:
                dic_p[data] += 1
            else:
                dic_p[data] = 1
        
        for data in completion:
            if dic_p[data] == 1:
                del dic_p[data]
            else:
                dic_p[data] -= 1

        answer = list(dic_p.keys())[0]

    return answer