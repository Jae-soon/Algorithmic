def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def solution(n):
    answer = 0
    for i in range(1, 11):
        result = factorial(i)
        
        if n >= result:
            answer = i
        
    return answer