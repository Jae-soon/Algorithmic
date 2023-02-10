def solution(phone_number):
    leng = len(phone_number) - 4

    answer = "*" * leng + phone_number[-4:]
    return answer