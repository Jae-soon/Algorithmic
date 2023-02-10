def solution(v):
    answer = []
    x = []
    y = []

    for i in v:
        if i[0] in x:
            x.remove(i[0])
        else:
            x.append(i[0])
        
        if i[1] in y:d
            y.remove(i[1])
        else:
            y.append(i[1])
    
    answer = x + y

    return answer