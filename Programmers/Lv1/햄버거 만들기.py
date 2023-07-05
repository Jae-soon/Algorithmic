from collections import deque

def solution(ingredient):
    answer = 0
    idx = 0
    li = []
    
    for i in ingredient:
        li.append(i)
        
        if li[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                li.pop()
            answer += 1
        
#     s = ''.join(list(map(str, ingredient)))
    
#     while '1231' in s:
#         answer += 1
#         for i in range(len(s)-3):
#             if '1231' == s[i:i+4]:
#                 s = s[:i] + s[i+4:]
#                 break

    return answer