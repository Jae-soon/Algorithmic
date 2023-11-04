def solution(elements):
    answer = 0
    origin_e = elements
    temp = [i for i in elements]
    elements = elements * 2
    
    for i in range(2, len(origin_e) + 1):
        find_elements = elements[:len(origin_e) + i - 1]
        for j in range(len(find_elements) - i + 1):
            temp.append(sum(find_elements[j:j+i]))

    answer = len(set(temp))
    return answer