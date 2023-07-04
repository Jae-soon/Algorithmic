def solution(s):
    answer = ''
    s_li = list(map(int, s.split(" ")))
    
    answer += str(min(s_li))
    answer += " "
    answer += str(max(s_li))

    return answer