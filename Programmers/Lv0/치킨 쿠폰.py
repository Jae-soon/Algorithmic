def solution(chicken):
    answer = -1
    plus_chicken = 0
    coupon_chicken = chicken // 10
    rest_coupon = chicken % 10
    coupon_chicken2 = coupon_chicken // 10
    rest_coupon2 = coupon_chicken % 10
    if rest_coupon + rest_coupon2 >= 10:
        plus_chicken += ((rest_coupon + rest_coupon2) // 10)
    
    answer = plus_chicken + coupon_chicken + coupon_chicken2
    
    return answer