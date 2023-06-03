def solution(d, budget):
    answer = 0
    d.sort()
    cnt = 0
    for i in d:
        cnt += i
        if cnt == budget:
            answer += 1
        if cnt >= budget:
            return answer
        answer += 1
        
    return answer