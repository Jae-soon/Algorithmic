def solution(s):
    answer = ''
    s = s.split(" ")
    s_li = []
    
    for word in s:
        if word:
            s_li.append(word[0].upper() + word[1:].lower())
        else:
            s_li.append(word)

    return " ".join(s_li)