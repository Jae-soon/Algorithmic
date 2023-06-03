from math import gcd

def lcm(n, m):
    for i in range(max(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            return i

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]

    return answer