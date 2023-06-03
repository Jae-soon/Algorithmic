def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    if answer < numbers[0] * numbers[1]:
        answer = numbers[0] * numbers[1]
    return answer