def solution(s):
    y_count = 0
    p_count = 0

    s = s.lower()
    
    for i in s:
        if "p" == i:
            p_count += 1

        if "y" == i:
            y_count += 1
    
            
    if y_count != p_count:
        return False
    else:
        return True