def solution(name, yearning, photo):
    answer = []
    n_hash = {}
    for i in range(len(name)):
        n_hash[name[i]] = yearning[i]
    
    for p in photo:
        sum = 0
        for i in range(len(p)):
            if p[i] in name:
                sum += n_hash[p[i]]
        answer.append(sum)
    return answer