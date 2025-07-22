import math

def solution(str1, str2):
    answer = 0
    
    str1_list = []
    str2_list = []
    for i in range(len(str1) - 1):
        str1_list.append(str1[i:i+2].lower())
        
    for i in range(len(str2) - 1):
        str2_list.append(str2[i:i+2].lower())
        
    if str1_list == [] or str2_list == []:
        return 65536
    
    str1_filtered = [x for x in str1_list if x.isalpha()]
    str2_filtered = [x for x in str2_list if x.isalpha()]
    
    str1_dict = {}
    str2_dict = {}
    
    for i in str1_filtered:
        if i in str1_dict:
            str1_dict[i] += 1
        else:
            str1_dict[i] = 1
    
    for i in str2_filtered:
        if i in str2_dict:
            str2_dict[i] += 1
        else:
            str2_dict[i] = 1

    intersection = set(str1_dict.keys()).intersection(set(str2_dict.keys()))
    union = set(str1_dict.keys()).union(set(str2_dict.keys()))
    
    intersection_count = 0
    union_count = 0
    
    for i in intersection:
        intersection_count += min(str1_dict.get(i, 0), str2_dict.get(i, 0))

    for i in union:
        union_count += max(str1_dict.get(i, 0), str2_dict.get(i, 0))
        
    answer = intersection_count / union_count if union_count != 0 else 1
         
    return math.floor(answer * 65536)