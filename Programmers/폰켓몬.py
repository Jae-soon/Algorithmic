def solution(nums):
    answer = 0
    getPocketmon = len(nums) // 2
    kind = len(set(nums))
    if kind <= getPocketmon:
        answer = kind
    else:
        answer = getPocketmon
    return answer