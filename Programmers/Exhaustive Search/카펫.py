from math import sqrt

def yaksu(n):
    yak = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            yak.append(i)
            if i ** 2 != n:
                yak.append(n // i)
    
    return sorted(yak)


def solution(brown, yellow):
    answer = []

    yak = yaksu(brown + yellow)

    if len(yak) % 2 == 0:
        idx_1 = int(len(yak) / 2)
        idx_2 = int(len(yak) / 2) - 1
    
    else:
        idx_1 = int(len(yak)/2)
        idx_2 = int(len(yak)/2)
    
    while 1:
        if (yak[idx_1] - 2) * (yak[idx_2] - 2) == yellow:
            return [yak[idx_1], yak[idx_2]]
        else:
            idx_1 += 1
            idx_2 -= 1

    return answer