def solution(score):
    answer = []
    li = []
    for i in score:
        li.append(sum(i) / 2)
    
    sort_li = sorted(li)
    sort_li.reverse()

    for i in li:
        answer.append(sort_li.index(i) + 1)
    return answer