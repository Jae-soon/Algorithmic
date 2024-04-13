def solution(s):
    answer = []
    s_slice = s[2:-2]
    
    s_split = s_slice.split("},{")
    s_split.sort(key=len)
    
    for i in s_split:
        i_split = i.split(",")
        
        for j in i_split:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer