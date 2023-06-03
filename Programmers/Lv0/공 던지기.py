def solution(numbers, k):
    answer = 0
    if len(numbers) / 2 <= k:
        numbers = numbers * k

    answer = numbers[(k - 1) * 2]
        
    return answer