def solution(n):
    answer = []
    a = []
    d = 2
    while d <= n:
        if n % d == 0:
            a.append(d)
            n = n / d
        else:
            d += 1

    for i in a:
        if i not in answer:
            answer.append(i)
        
    return answer