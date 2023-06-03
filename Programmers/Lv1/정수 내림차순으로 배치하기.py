def solution(n):
    list_n = list(str(n))

    list_n.sort(reverse=True)
    
    answer = int("".join(list_n))

    return answer