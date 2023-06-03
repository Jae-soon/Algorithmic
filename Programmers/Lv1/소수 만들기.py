from itertools import combinations
from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solution(nums):
    num_combinations = [sum(comb) for comb in list(combinations(nums, 3)) if is_prime(sum(comb))]

    return len(num_combinations)