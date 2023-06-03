def solution(clothes):
    answer = 0
    clothes_dict = {}
    for i in clothes:
        clothes_dict[i[1]] = []
    
    for i in clothes:
        clothes_dict[i[1]].append(i[0])
    
    sum1 = 1

    for i in clothes_dict.keys():
        sum1 *= (1 + len(clothes_dict[i]))

    answer = sum1 - 1

    return answer