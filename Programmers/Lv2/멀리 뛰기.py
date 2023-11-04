def solution(n):
    answer = 0

    if n < 3:
        return n
    
    distance = [0] * (n + 1)
    distance[1] = 1
    distance[2] = 2

    for i in range(3, n+1):
        distance[i] = distance[i - 1] + distance[i - 2]

    return distance[n] % 1234567