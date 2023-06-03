import collections

def solution(N, stages):
    stop = collections.Counter(stages) # 각 원소의 개수 구하기
    fail = collections.defaultdict(float) # float형의 fail 리스트 생성

    fail[1] = len(stages)
    for i in range(1, N + 1):
        if fail[i] != 0:
            fail[i + 1] = fail[i] - stop[i]
            fail[i] = stop[i] / fail[i]

    if N + 1 in fail:
        del fail[N + 1]
    return sorted(fail, key=lambda x: -fail[x])

# def solution(N, stages):
#     answer = []
#     dic = {}

#     for i in range(1, N + 1):
#         not_pass = 0
#         for j in stages:
#             if i == j:
#                 not_pass += 1
        
#         dic[i] = (not_pass / len(stages))
#         while i in stages:
#             stages.remove(i)
    
#     sort_answer = sorted(dic.items(), key = lambda x : x[1], reverse=True)
    
#     for i in sort_answer:
#         answer.append(i[0])
    
#     return answer