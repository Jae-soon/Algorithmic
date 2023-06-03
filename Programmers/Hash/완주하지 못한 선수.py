def solution(participant, completion):
    answer = ''
    com_dict = {}
    for i in participant:
        com_dict[i] = 0
    
    for i in participant:
        com_dict[i] += 1
    
    for i in completion:
        com_dict[i] -= 1

    for k, v in com_dict.items():
        if v == 1:
            answer = k
        
    return answer