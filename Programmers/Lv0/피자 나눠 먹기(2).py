def solution(n):

    answer = 1
    
    while 1:
        if (6 * answer) % n == 0:
            break
        
        answer += 1 

    answer = 0
    x = 1

    while 1:
        if (6 * x) % n == 0:
            return x
        else:
            x += 1

    return answer