def factorial(n):
    num = 1
    for i in range(n):
        num *= (i + 1)
    
    return num

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer