def solution(lines):
    line = {}
    answer = 0

    for i in lines:
        for j in range(i[0], i[1]):
            line[j] = 0

    for i in lines:
        for j in range(i[0], i[1]):
            line[j] += 1
    
    for key in line.keys():
        if line[key] > 1:
            answer += 1

    return answer