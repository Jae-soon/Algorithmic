def solution(n):
    answer = 0
    x = 1

    while 1:
        if (6 * x) % n == 0:
            return x
        else:
            x += 1
    return answer