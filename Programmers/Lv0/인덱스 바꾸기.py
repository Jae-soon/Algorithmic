def solution(my_string, num1, num2):
    answer = ''
    
    #num1_str = my_string[num1]
    #num2_str = my_string[num2]
    #my_string.replace(num1_str, num2_str)
    #my_string.replace(num1_str, num2_str)
    
    #my_string.insert(num2_str, num1)
    #my_string.insert(num1_str, num2)
    
    #return my_string
    str_list = list(my_string)
    num1_str = str_list[num1]
    num2_str = str_list[num2]
    str_list[num1] = num2_str
    str_list[num2] = num1_str
    answer = ''.join(str_list)
    return answer
