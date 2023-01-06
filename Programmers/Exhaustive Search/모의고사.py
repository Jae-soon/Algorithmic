def solution(answers):
    student_1 = [1, 2, 3 ,4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0 ,0]
    answer = []

    for i, j in enumerate(answers):
        if student_1[i % len(student_1)] == j:
            score[0] += 1
        
        if student_2[i % len(student_2)] == j:
            score[1] += 1

        if student_3[i % len(student_3)] == j:
            score[2] += 1
    
    for i, j in enumerate(score):
        if max(score) == score[i]:
            answer.append(i + 1)
    return answer