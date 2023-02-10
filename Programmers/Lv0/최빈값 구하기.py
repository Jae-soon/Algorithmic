def solution(array):
    answer = 0
    num_dict = {}
    sort_arr = sorted(array)
    for i in sort_arr:
        num_dict[i] = 0
    
    for i in array:
        num_dict[i] += 1
    
    li = [k for k, v in num_dict.items() if max(num_dict.values()) == v]
    if len(li) > 1:
        return -1
    else:
        answer = li[0]
    return answer