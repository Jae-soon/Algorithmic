import math

def solution(str1, str2):
    answer = 0
    str1_li = []
    str2_li = []
    same_list = []
    diff_list = []

    for i in range(0, len(str1) - 1):
        if str1[i:i+2].upper().isalpha():
            str1_li.append(str1[i:i+2].upper())
    
    for i in range(0, len(str1) - 1):
        if str2[i:i+2].upper().isalpha():
            str2_li.append(str2[i:i+2].upper())

    for i in str1_li:
        if i in str2_li:
            same_list.append(i)
        else:
            diff_list.append(i)
    
    for i in str2_li:
        if i not in str1_li:
            diff_list.append(i)
    
    diff_list = same_list + diff_list

    if len(same_list) == 0 or len(diff_list) == 0:
        answer = 1
    else:
        answer = math.floor((len(same_list) / (len(diff_list) + len(same_list))) * 65536)
        
    return answer