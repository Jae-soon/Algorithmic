def solution(order):
    answer = 0
    order_list = map(int, list(str(order)))
    num_list = [3, 6, 9]
    for i in order_list:
        for j in num_list:
            if i == j:
                answer += 1
    return answer