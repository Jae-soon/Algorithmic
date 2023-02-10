def solution(absolutes, signs):
    answer = 0
    for i, value in enumerate(signs):
        if value:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer