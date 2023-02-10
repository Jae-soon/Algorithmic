def solution(lottos, win_nums):
    answer = []

    can = {0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : 1}
    cnt = 0
    zero_count = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        
        if i == 0:
            zero_count += 1

    if can[cnt] == 1:
        answer.append(can[cnt + zero_count])
        answer.append(can[cnt])
    elif can[cnt] == 2:
        answer.append(can[cnt + zero_count])
        answer.append(can[cnt])
    elif can[cnt] == 5:
        answer.append(can[cnt + zero_count])
        answer.append(can[cnt])
    elif can[cnt] == 6:
        answer.append(can[cnt + zero_count])
        answer.append(can[cnt])
    else:
        answer.append(can[cnt + zero_count])
        answer.append(can[cnt])
    

    return answer