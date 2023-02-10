def measure(n):
    measure = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            measure.append(i)
            if (i ** 2) != n: # 제곱값인지 구하기
                measure.append(n // i)
    return len(measure)

def solution(number, limit, power):
    answer = 0
    knight = []

    for i in range(1, number + 1):
        if measure(i) <= limit:
            knight.append(measure(i))
        else:
            knight.append(power)
    
    return sum(knight)