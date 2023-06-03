def solution(arrA, arrB):
    answer = True

    for _ in range(len(arrA)):
        if arrA == arrB:
            return True
        i = arrA.pop(0)
        arrA.append(i)
        
        
    return False