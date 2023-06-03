def solution(num):
    answer = 0

    c_num = num
    while 1:    
        if c_num == 1:
            return answer

        if answer > 500:
            return -1
        
        if c_num % 2 == 0:
            c_num /= 2
            answer += 1
        else:
            c_num = c_num * 3 + 1
            answer += 1
    
    return answer