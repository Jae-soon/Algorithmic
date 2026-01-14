def solution(dirs):
    already_move_list = [(0, 0)]
    moving = []
    (default_x, default_y) = (0, 0)
    
    move = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }
    
    for dir in dirs:
        (x, y) = move[dir]
        
        if default_x + x > 5 or default_x + x < -5:
            x = 0
        
        if default_y + y > 5 or default_y + y < -5:
            y = 0
        
        default_x = default_x + x
        default_y = default_y + y
        
        already_move_list.append((default_x, default_y))
    
    for i in range(len(already_move_list) - 1):
        if already_move_list[i] != already_move_list[i+1]:
            moving.append((already_move_list[i], already_move_list[i+1]))
    
    count = 0
    already_check = []
    for m in moving:
        move_a, move_b = m
        already_check.append(m)
        if (move_b, move_a) in moving and (move_b, move_a) not in already_check:
            count += 1
            already_check.append((move_b, move_a))
    
    return len(list(set(moving))) - count