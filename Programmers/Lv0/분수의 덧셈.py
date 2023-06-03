from math import gcd

def lcm(num1, num2):
    if num1 < num2:
        max = num2
    else:
        max = num1
    
    for i in range(max, (num1 * num2) + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i

def solution(denum1, num1, denum2, num2):
    answer = []

    if num1 == num2:
        answer = [denum1 + denum2, num1]
    else:
        n = lcm(num1, num2)
        answer = [denum1 * int((n / num1)) + denum2 * int((n / num2)), n]
    
    n = int(gcd(answer[0], answer[1]))

    if answer[0] % n == 0 and answer[1] % n == 0:
        answer[0] = answer[0] / n
        answer[1] = answer[1] / n 

    if answer[0] == answer[1]:
        answer = [1, 1]
    
    return answer