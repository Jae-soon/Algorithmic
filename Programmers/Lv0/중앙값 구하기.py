def solution(array):
    answer = 0
    len_arr = int(len(array))
    array.sort()
    answer = array[int(len_arr / 2)]
    return answer