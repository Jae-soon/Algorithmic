def s(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return rev_base[::-1] 

def solution(n):    
    num = s(n)
    n_list = list(num)
    n_list.reverse()

    n_ = "".join(n_list)

    return int(n_, 3)