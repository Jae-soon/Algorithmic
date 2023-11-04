from collections import defaultdict

def solution(k, tangerine):
    kind_dict = defaultdict(int)

    for i in tangerine:
        kind_dict[i] += 1
    kind_dict = dict(kind_dict)
    kind_dict = sorted(kind_dict.items(), key=lambda i : i[1], reverse=True)
    
    sum = 0
    temp = []
    for (i, v) in kind_dict:
        if v >= k:
            return 1
        sum += v
        temp.append(i)
        if sum >= k:
            break
    return len(temp)