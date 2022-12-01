def solution(my_string, num1, num2):
    answer = ''
    str_list = list(my_string)
    num1_str = str_list[num1]
    num2_str = str_list[num2]
    str_list[num1] = num2_str
    str_list[num2] = num1_str
    answer = ''.join(str_list)
    return answer