def solution(common):
    answer = 0
    n = common[1] - common[0]
    if common[1] + n == common[2]:
        return common[-1] + n
    else:
        if common[0] == 1:
            return common[-1] * (common[-1] / common[-2])
        else:
            return common[-1] * n