def solution(emergency):
    answer = []
    set_list = sorted(emergency)
    set_list.reverse()
    for i in emergency:
        answer.append(set_list.index(i) + 1)
    return answer