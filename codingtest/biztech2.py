from collections import Counter

def solution(s):
    answer = 0

    counter  = Counter(s)
    
    for i in counter.keys():
        if counter[i] % 2 == 1:
            answer += 1
    
    return answer