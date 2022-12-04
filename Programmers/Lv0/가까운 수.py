def solution(array, n):
    answer = 0
    min = 100
    for i in array:
        if min > abs(i - n):
            min = abs(i - n)
            answer = i
    return answe