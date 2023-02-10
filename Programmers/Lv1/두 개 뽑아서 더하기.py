from itertools import combinations

def solution(numbers):
    num_combinations = [sum(comb) for comb in list(combinations(numbers, 2))]
    answer = list(set(num_combinations))
    answer.sort()

    return answer