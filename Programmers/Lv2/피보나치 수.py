# 시간 복잡도 확인
# 재귀함수 사용 시 오랜시간 사용
# 피보나치의 로직 파악(현재 = 현재 + 이전 / 이전 = 현재 로 2 ~ n까지 반복)
def solution(n):
    answer = 1
    pre = 0
    
    for _ in range(2, n+1):
        answer, pre = answer + pre, answer

    return answer % 1234567