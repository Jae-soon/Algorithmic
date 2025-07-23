def solution(topping):
    answer = 0
    
    topping_target = set()
    topping_list = {}
    
    # 전체 Topping별 Count을 담음
    for i in topping:
        topping_list[str(i)] = topping_list.get(str(i), 0)
        topping_list[str(i)] += 1
    
    for i in topping:
        # 비교 대상에 topping 추가(중복 제거)
        topping_target.add(i)
        
        # topping_list에 담긴 topping count를 1개씩 줄임
        topping_list[str(i)] -= 1
        
        # 실제 topping 수가 0개가 되면 topping_list 삭제
        if topping_list[str(i)] == 0:
            del topping_list[str(i)]
        if len(topping_target) == len(topping_list.keys()):
            answer += 1
    return answer