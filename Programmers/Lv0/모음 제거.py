def solution(my_string):
    answer = ''
    alphabet = ['a', 'e', 'i', 'o', 'u']

    for i in my_string:
        if i in alphabet:
            continue
        answer += i

    return answer

print(solution("nice to meet you"))