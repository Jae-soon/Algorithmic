def solution(k, m, score):
    answer = 0
    box = []
    score = sorted(score, reverse=True)
    for i in range(0, len(score) - 2, m):
        box.append(score[i:i + m])
    
    for i in box:
        if len(i) == m:
            answer += min(i) * len(i)

    return answer