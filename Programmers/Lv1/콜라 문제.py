def solution(a, b, n):
    answer = 0
    plus_cola = 0
    rest_cola = n
    
    while rest_cola >= a:
        plus_cola = (rest_cola // a) * b # 얻는 콜라
        rest_cola = rest_cola % a + plus_cola # 남은 콜라
        answer += plus_cola

    
    return answer