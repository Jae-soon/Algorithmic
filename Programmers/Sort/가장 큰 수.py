def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x * 3, reverse=True) # ASCII 사용
    print(lambda x : x * 3)
    return str(int("".join(numbers)))