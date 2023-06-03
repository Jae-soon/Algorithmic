def solution(arr):
    arr = sorted(arr)
    cnt = 0

    for i in range(len(arr)):
        if arr[i] == i + 1:
            cnt += 1
    
    if cnt == len(arr):
        return True

    return False