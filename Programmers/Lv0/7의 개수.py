def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            if 7 == int(j):
                answer += 1
    return answer