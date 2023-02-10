def solution(board, moves):
    answer = 0
    rest = []

    for i in moves:
        temp = i - 1
        for j in range(len(board)):
            if board[j][temp] != 0:
                rest.append(board[j][temp])
                if len(rest) >= 2:
                    if rest[-2] == rest[-1]:
                        rest.pop()
                        rest.pop()
                        answer += 1
                board[j][temp] = 0
                break

    return answer * 2