def solution(keyinput, board):
    answer = [0, 0]
    dic = {
        "left" : [-1, 0],
        "right" : [1, 0],
        "up" : [0, 1],
        "down" : [0, -1]
    }
    for i in keyinput:
        answer[0] += dic[i][0]
        answer[1] += dic[i][1]

        if abs(answer[0]) > (board[0] // 2):
            answer[0] -= dic[i][0]
            
        if abs(answer[1]) > (board[1] // 2):
            answer[1] -= dic[i][1]
        print(answer)

    return answer