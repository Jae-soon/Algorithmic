# 정답
def solution(park, routes):
    answer = []

    h = len(park)
    w = len(park[0])
    x, y = 0, 0

    nav = {
        'S' : [1, 0],
        'N' : [-1, 0],
        'W' : [0, -1],
        'E' : [0, 1]
    }

    # start 부분 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = i
                y = j

    for route in routes:
        direc, distance = route.split()[0], int(route.split()[1])
        flag = 0
        step_x = x
        step_y = y

        # 장애물 피하기
        for i in range(1, distance + 1):
            step_x += nav[direc][0]
            step_y += nav[direc][1]

            if step_x >= h or step_x <= -1 or step_y >= w or step_y <= -1 or park[step_x][step_y] == "X":
                flag = 1
                break

        if flag == 0:
            x += nav[direc][0] * distance
            y += nav[direc][1] * distance
        
    answer = [x, y]
    return answer


# 틀린 답
def solution(park, routes):
    answer = []

    # start 좌표 구하기
    start = []
    idx = 0

    for p in park:
        if "S" in p:
            i = p.find("S")
            start = [idx, i]
            break
        idx += 1

    for route in routes:
        direc, move = route.split(" ")[0], int(route.split(" ")[1])

        if direc == "E":
            start = [start[0], start[1] + move]
            
            if start[0] < 0 or start[0] > len(route) - 1 or start[1] < 0 or start[1] > len(routes) - 1:
                start = [start[0], start[1] - move]
                continue
            
            for i in range(move):
                if park[start[0]][start[1] - i] == "X":
                    start = [start[0], start[1] - move]
                    break
        
        elif direc == "W":
            start = [start[0], start[1] - move]

            if start[0] < 0 or start[0] > len(route) - 1 or start[1] < 0 or start[1] > len(routes) - 1:
                start = [start[0], start[1] + move]
                continue
                
            for i in range(move):
                if park[start[0]][start[1] + i] == "X":
                    start = [start[0], start[1] + move]
                    break

        elif direc == "S":
            start = [start[0] + move, start[1]]

            if start[0] < 0 or start[0] > len(route) - 1 or start[1] < 0 or start[1] > len(routes) - 1:
                start = [start[0] - move, start[1]]
                continue
                
            for i in range(move):
                if park[start[0] - i][start[1]] == "X":
                    start = [start[0] - move, start[1]]
                    break

        else:
            start = [start[0] - move, start[1]]

            if start[0] < 0 or start[0] > len(route) - 1 or start[1] < 0 or start[1] > len(routes) - 1:
                start = [start[0] + move, start[1]]
                continue
                
            for i in range(move):
                if park[start[0] + i][start[1]] == "X":
                    start = [start[0] + move, start[1]]
                    break

    return start