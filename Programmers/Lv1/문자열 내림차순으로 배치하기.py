def solution(s):
    upper_list = []
    lower_list = []

    for i in s:
        if i.isupper():
            upper_list.append(i)
        else:
            lower_list.append(i)     

    upper_list.sort(reverse=True)
    lower_list.sort(reverse=True)

    answer = "".join(lower_list + upper_list)
    return answer