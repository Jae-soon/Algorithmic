def solution(n):
    answer = 0
    binary_count = bin(n).count("1")

    for i in range(n+1, 1000001):
        if bin(i).count("1") == binary_count:
            answer = i
            break

    return answer