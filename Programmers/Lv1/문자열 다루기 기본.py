def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
        return answer
    else:
        return False
    # try:
    #     if int(s):
    #         return True
    # except:
    #     return False
