def solution(numbers, target):
    answer = 0
    def dfs(i, s, numbers, target):
        nonlocal answer
        if i == len(numbers):
            if s == target:
                answer += 1
            return
        dfs(i + 1, s + numbers[i], numbers, target)
        dfs(i + 1, s - numbers[i], numbers, target)

    dfs(0, 0, numbers, target)
    return answer