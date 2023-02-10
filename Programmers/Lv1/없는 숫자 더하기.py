def solution(numbers):
    not_exist = []
    for i in range(10):
        if i not in numbers:
            not_exist.append(i)
    return sum(not_exist)