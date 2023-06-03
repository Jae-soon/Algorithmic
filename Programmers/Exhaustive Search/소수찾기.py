from itertools import permutations

def sosu(num):
    count = 0
    for i in range(2, int((num ** 0.5)) + 1):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    permutation = []
    already_exist = []
    for i in range(1, len(numbers) + 1):
        permutation += list(permutations(num_list, i)) # num_list의 숫자들을 순열조합
    
    new = [int("".join(p)) for p in permutation]

    for i in new:
        if i < 2:
            continue
        if sosu(i) and i not in already_exist:
            answer += 1
            already_exist.append(i)
    

    return answer