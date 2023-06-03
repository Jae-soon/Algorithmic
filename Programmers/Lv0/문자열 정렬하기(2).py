def solution(my_string):
    answer = ''
    answer = my_string.lower()
    str_list = list(answer)
    str_list.sort()
    answer = ''.join(str_list)
    return answer