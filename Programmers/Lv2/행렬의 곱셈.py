import numpy as np

def solution(arr1, arr2):
    answer = []
    
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    
    new_arr = arr1 @ arr2
    
    for i in new_arr:
        answer.append(i.tolist())
    
    return answer