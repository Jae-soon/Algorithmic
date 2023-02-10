def solution(n):
    answer = []
    
    week = n // 7 # 몇주가 지났는지 확인
    day = n % 7 # 몇주 + 남은 기간을 활용
    
    if day == 0:
        answer = [week * 2, week * 2]
    elif day == 6:
        answer = [week * 2 + 1, week * 2 + 2]
    elif day == 1:
        answer = [week * 2, week * 2 + 1]
    else:
        answer = [week * 2, week * 2 + 2]

    return answer