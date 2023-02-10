def solution(arr):
    min_arr = min(arr)
    arr.remove(min_arr)

    if len(arr) == 0:
        return [-1]
    return arr