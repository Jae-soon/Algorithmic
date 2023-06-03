def solution(dots):
    answer = 0

    d1, d2, d3, d4 = dots
    # 1, 2 기울기
    ans1 = (d1[1] - d2[1]) / (d1[0] - d2[0])
    # 3, 4
    ans2 = (d3[1] - d4[1]) / (d3[0] - d4[0]) 
    # 1, 3
    ans3 = (d1[1] - d3[1]) / (d1[0] - d3[0]) 
    # 2, 4
    ans4 = (d2[1] - d4[1]) / (d2[0] - d4[0])
    # 2, 3
    ans5 = (d2[1] - d3[1]) / (d2[0] - d3[0])
    # 1, 4
    ans6 = (d1[1] - d4[1]) / (d1[0] - d4[0])

    if ans1 == ans2 or ans3 == ans4 or ans5 == ans6:
        return 1
    
    return answer