def solution(numbers, direction):
    if direction == "right":
        pop_num = numbers.pop()
        numbers.insert(0, pop_num)
    else:
        pop_num = numbers[0]
        numbers.remove(pop_num)
        numbers.append(pop_num)
    return numbers