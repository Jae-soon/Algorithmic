def solution(want, number, discount):
    answer = 0
    want_dict = dict()
    
    # 원하는 제품의 개수 dictionary 형태로 저장
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        temp_dict = want_dict.copy()
        
        conv_discount = discount[i:i+10]
        
        for d in conv_discount:
        
            if d in temp_dict.keys():
                temp_dict[d] -= 1
        
        if not any(e != 0 for e in list(temp_dict.values())):
            answer += 1
        
    return answer