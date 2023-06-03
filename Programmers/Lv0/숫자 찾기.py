def solution(num, k):
    answer = 0
    num_list = list(str(num))
    try:
        answer = num_list.index(str(k)) + 1
    except ValueError:
        answer = -1
    return answer