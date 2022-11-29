def solution(numbers):
    new_list = []
    max = 0
    while True:
        for i in numbers:
            if i > max:
                max = i
        new_list.append(max)
        numbers.remove(max)
        max = 0
        
        if len(numbers) == 0:
            break
    print(new_list)
    answer = new_list[0] * new_list[1]
    return answer