def solution(num_list):
    answer = []
    count2 = 0
    count3 = 0
    for i in num_list:
        if i % 2 == 0:
            count2 += 1
        elif i % 2 == 1:
            count3 += 1
    
    answer.append(count2)
    answer.append(count3)
    return answer