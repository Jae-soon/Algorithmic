def solution(sizes):
    answer = 0
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    width_max = max(width)
    height_max = max(height)
    answer = width_max * height_max
    return answer