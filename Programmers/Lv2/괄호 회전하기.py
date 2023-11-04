from collections import defaultdict, deque

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        d = defaultdict(int)
        s_2 = s * 2
        s_temp = s_2[0 + i:len(s) + i]
        
        dq = deque()
        dq.append("0")
        for i in list(s_temp):
            if i == "{" or i == "(" or i == "[":
                dq.append(i)
            elif i == "}":
                dp = dq.pop()
                if dp == "{":
                    continue
                else:
                    if "{" not in dq:
                        dq.append("0")
                    dq.append(dp)
            elif i == "]":
                dp = dq.pop()
                if dp == "[":
                    continue
                else:
                    if "[" not in dq:
                        dq.append("0")
                    dq.append(dp)
            elif i == ")":
                dp = dq.pop()
                if dp == "(":
                    continue
                else:
                    if "(" not in dq:
                        dq.append("0")
                    dq.append(dp)
        if len(dq) == 1:
            answer += 1
            
        # 테케 4번까지 정답
        # n = 0
        # for i in list(s_temp):
        #     if (i == "{" and d["{"] != -1) or (i == "(" and d["("] != -1) or (i == "[" and d["["] != -1):
        #         d[i] += 1
        #     elif i == "}":
        #         d["{"] -= 1
        #     elif i == "]":
        #         d["["] -= 1
        #     elif i == ")":
        #         d["("] -= 1

        # for i in list(d.values()):
        #     if i == 0:
        #         n += 1
        
        # if n == len(d):
        #     answer += 1
        

    return answer