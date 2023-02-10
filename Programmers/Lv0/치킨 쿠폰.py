def solution(chicken):
    c = chicken
    answer = 0

    while c >= 10:
        service = c // 10
        rest_coupon = c % 10
        answer += service
        c = service + rest_coupon

    return answer