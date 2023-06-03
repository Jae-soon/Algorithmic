def solution(x):
    x_sum = 0
    list_x = list(str(x))

    for i in list_x:
        x_sum += int(i)
    
    if x % x_sum == 0:
        return True
    else:
        return False
