C = int(input())

for _ in range(C):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    cnt = 0

    for personal_score in score[1:]:
        if personal_score > avg:
            cnt += 1
    rate = cnt / score[0] * 100
    print(f'{rate:.3f}%') 