visit = []
answer = 0

def find(alien_list, depth, b):
    depth = 0
    for ailen in alien_list:
        left, right = ailen
        
        for i in range(left, right):
            if i in b:
                b.remove(i)
                depth += 1
    
    return depth

def solution(n, x, a, b):
    
    alien_list = list(list())

    for i in range(n):
        alien_list.append([x[i] - a[i], x[i] + a[i]])

    for i in range(n):
        depth = find(alien_list, 1, b)

    return max(answer, depth)

n = 5
x = [3, 2, 8, 5, 3]
a = [4, 2, 4, 3, 1]
b = [2, 13, 12, 5, 10]

solution(n, x, a, b)