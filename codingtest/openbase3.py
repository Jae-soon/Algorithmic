def solution(numbers):
    answer = 0
    def dfs(i, s, numbers):
        nonlocal answer
        if i == len(numbers):
            if s == 0:
                answer += 1
            return
        dfs(i + 1, s + numbers[i], numbers)
        dfs(i + 1, s - numbers[i], numbers)

    dfs(0, 0, numbers)
    return answer