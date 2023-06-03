def solution(array, n):
    answer = 0
    min = 100
    for i in array:
        if min > abs(i - n):
            min = abs(i - n)
            answer = i
        elif min == abs(i - n):
            if answer > i:
                answer = i
    return answer