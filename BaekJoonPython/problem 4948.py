import sys

def prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

problem_list = list(range(2, 123456 * 2))
memo = list()

for i in problem_list:
    if prime(i):
        memo.append(i)

n = sys.stdin.readline();

while True:
    count = 0
    if n == 0:
        break

    for i in memo:
        if n < i <= 2 * n:
            count += 1
        
    print(count)
    n = sys.stdin.readline()
