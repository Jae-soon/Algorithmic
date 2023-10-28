def solution(n):
    answer = 1
    pre = 0
    
    for _ in range(2, n+1):
        answer, pre = answer + pre, answer

    return answer % 1234567