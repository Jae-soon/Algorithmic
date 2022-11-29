import math

def solution(num1, num2):
    answer = (num1 / num2) * 1000
    answer = math.trunc(answer)
    return answer