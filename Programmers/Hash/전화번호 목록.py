def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        if i + 1 >= len(phone_book):
            break
        
        if len(phone_book[i + 1]) > len(phone_book[i]):
            if phone_book[i + 1].find(phone_book[i]) == 0:
                return False
    return answer
