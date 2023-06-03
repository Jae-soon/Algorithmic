def solution(polynomial):
    answer = ''
    h = polynomial.split(" + ")
    
    x1 = 0
    x_ = 0

    for i in h:
        if 'x' in i:
            if i[0] == 'x':
                x1 += 1
            else:
                x1 += int(i.strip('x'))
        else:
            x_ += int(i)

    if x1 > 1:
        if x_ != 0:
            answer = str(x1) + "x + " + str(x_)
        else:
            answer = str(x1) + "x"
    elif x1 == 1:
        if x_ != 0:
            answer = "x + " + str(x_)
        else:
            answer = "x"
    else:
        if x_ != 0:
            answer = str(x_)
        else:
            answer = '0'

    return answer