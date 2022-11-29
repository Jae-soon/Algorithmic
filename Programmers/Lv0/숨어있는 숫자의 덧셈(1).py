import re

def solution(my_string):
    answer = 0
    str = re.findall(r'\d', my_string)
    
    for i in str:
        answer += int(i)
    return answer 