def solution(nums):
    answer = 0
    nums_count = len(nums) / 2
    set_nums = set(nums)
    if len(set_nums) <= nums_count:
        answer = len(set_nums)
    else:
        answer = nums_count
    return answer