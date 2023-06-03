def solution(spell, dic):
    answer = 2
    
    
    for i in dic:
        dic = {i : 0 for i in spell}
        count = 0
        for j in spell:
            if j in i:
                dic[j] += 1
            
            if dic[j] == 1:
                count += 1
            
            if count == len(spell):
                answer = 1
        
        
    return answer