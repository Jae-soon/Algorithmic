def make1(s):
    s_li = list(s)
    new_li = []
    zero_count = 0
    for i in s_li:
        if i == "1":
            new_li.append("1")
        else:
            zero_count += 1
    return new_li, zero_count

def make_bin(s):
    return bin(len(s))[2:]

def solution(s):
    answer = []
    zc = 0
    count = 0
    while "1" != s:
        count += 1
        li, zero_count = make1(s)
        zc += zero_count
        s = make_bin(li)
    
    answer = [count, zc]
    

    return answer