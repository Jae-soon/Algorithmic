def solution(cipher, code):
    answer = ''

    for i in range(0, len(cipher) + 1, code):
        if i == 0:
            continue
        answer += cipher[i-1]

    return answer