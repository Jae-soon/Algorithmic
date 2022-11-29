def solution(n, k):
    count = 0
    if n >= 10:
        count = n // 10
        answer = 12000 * n + 2000 * (k - count)
    else:
        answer = 12000 * n + 2000 * k
    return answer