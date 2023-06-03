def solution(k, score):    
    answer = []
    li = []

    for i in score:
        if len(li) == k:
            if min(li) < i:
                li.remove(min(li))
                li.append(i)
        else:
            li.append(i)
        
        answer.append(min(li))

    return answer