def solution(num, total):
    answer = []
    
    middle = total // num
    sub = 0
    
    if total % num == 0:
        sub = int(num / 2)
    else:
        sub = int(num / 2) - 1
    
    start = middle - sub

    for i in range(num): 
        answer.append(start + i)

    return answer