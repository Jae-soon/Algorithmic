def solution(phone_book):
    answer = True

    phone_book.sort()
    book_len = len(phone_book)
    for i in range(book_len):
        if i + 1 >= book_len:
            break

        if len(phone_book[i + 1]) > len(phone_book[i]):
            if phone_book[i + 1].find(phone_book[i]) == 0:
                return False

    return True