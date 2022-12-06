def solution(bin1, bin2):
    answer = ''
    
    a = int("0b" + bin1, 2)
    b = int("0b" + bin2, 2)

    answer = str(bin(a + b))
    answer = answer[2:]

    return answer