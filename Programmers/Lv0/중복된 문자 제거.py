def solution(my_string):
    answer = ''
    new_str_list = []
    str_list = list(my_string)
    for i in str_list:
        if i not in new_str_list:
            answer += i
            new_str_list.append(i)
    return answer