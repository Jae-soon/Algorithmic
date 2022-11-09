def solution(sizes):
    width = 0
    height = 0

    for i in range(len(sizes)):
        sizes[i].sort()
    print(sizes)

    for i in range(len(sizes)):
        if width < sizes[i][0]:
            width = sizes[i][0]
            print("width = " + str(width))

    for i in range(len(sizes)):
        if height < sizes[i][1]:
            height = sizes[i][1]
            print("height = " + str(height))

    area = width * height
    return area

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
solution(sizes)