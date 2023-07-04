def solution(ingredient):
    answer = 0
    
    s = ''.join(list(map(str, ingredient)))
    
    while '1231' in s:
        print(s)
        for i in range(len(s)-4):
            if '1231' == s[i:i+4]:
                s = s[:i] + s[i+4:]
                break
    
    
    return answer