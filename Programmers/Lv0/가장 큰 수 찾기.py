def solution(array):
    answer = []
    max_value = max(array)
    answer.append(max_value)
    answer.append(array.index(max_value))
    return answer