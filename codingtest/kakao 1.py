def solution(flowers):
    answer = 0
    day_list = []
    for arr in flowers:
        for i in range(arr[0], arr[1]):
            day_list.append(i)
        
    set_list = set(day_list)
    answer = len(set_list)

    return answer

flowers = [[3, 4], [4, 5], [6, 7], [8, 10]]
print(solution(flowers))