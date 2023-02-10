def solution(price, money, count):
    answer = -1
    sum_money = 0

    for i in range(1, count + 1):
        sum_money += price * i
    
    if money >= sum_money:
        return 0

    return sum_money - money