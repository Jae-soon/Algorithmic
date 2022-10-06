from collections import deque

def solution(numbers, target):
    q = deque()
    count = 0
    num_len = len(numbers) # 4
    q.append([numbers[0], 0]) # [4, 0]
    q.append([-1 * numbers[0], 0]) # [4,0], [-4,0]

    while q:
        num, index = q.popleft() # 4, 0 / -4, 0 / 
        index += 1 # 4, 1 / -4, 1 / 
        if index == num_len and num == target: 
            count += 1
        
        if index < num_len:
            q.append([num + numbers[index], index]) # [-4, 0], [5, 1] / 
            q.append([num - numbers[index], index]) # [-4, 0], [5, 1], [3, 1] / 
   
    return count



numbers = [4, 1, 2, 1]
target = 2

print(solution(numbers, target))

