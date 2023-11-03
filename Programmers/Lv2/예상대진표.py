def is_even(n):
    if n % 2 == 0:
        return True
    return False

def solution(n,a,b):
    answer = 0
    
    while 1:
        if a == b:
            return answer
        
        if is_even(a):
            a = a // 2
        else:
            a = a // 2 + 1

        if is_even(b):
            b = b // 2
        else:
            b = b // 2 + 1
            
        answer += 1
    