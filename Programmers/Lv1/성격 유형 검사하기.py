def solution(survey, choices):
    answer = ''
    
    score = {'A' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'N' : 0, 'R' : 0, 'T' : 0}

    for i in range(len(survey)):
        if choices[i] > 4:
            score[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            score[survey[i][0]] += 4 - choices[i]
    
    if score['T'] > score['R']:
        answer += 'T'
    else:
        answer += 'R'
    
    if score['F'] > score['C']:
        answer += 'F'
    else:
        answer += 'C'

    if score['M'] > score['J']:
        answer += 'M'
    else:
        answer += 'J'
    
    if score['N'] > score['A']:
        answer += 'N'
    else:
        answer += 'A'


    return answer