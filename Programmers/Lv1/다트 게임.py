def solution(dartResult):
    dart = ""
    score = []

    for i in dartResult:
        if i.isdigit():
            dart += i
        elif i == "S":
            dart = int(dart) ** 1
            score.append(dart)
            dart = ""
        elif i == "D":
            dart = int(dart) ** 2
            score.append(dart)
            dart = ""
        elif i == "T":
            dart = int(dart) ** 3
            score.append(dart)
            dart = ""
        elif i == "*":
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        else:
            score[-1] = -score[-1]

    return sum(score)