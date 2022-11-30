import re

def solution(my_string):
    answer = []
    number = re.findall(r'\d', my_string)
    print(number)
    
    for i in number:
        answer.append(int(i))
    
    answer.sort()
    
    return answer