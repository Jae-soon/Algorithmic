import sys

inf = sys.stdin
n = int(inf.readline())

buildings = list(map(int, input().split()))
result = 0
# 기울기
def gradient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

for i1, y1 in enumerate(buildings):
    x1 = i1 + 1
    right = 0
    can_see_right = None
    for i2 in range(i1+1, n+1):
        if i2 == n:
            break
        
        x2 = i2 + 1
        y2 = buildings[i2]
        gradient_right = gradient(x1, y1, x2, y2)
        
        if can_see_right is None or can_see_right < gradient_right:
            can_see_right = gradient_right
            right += 1
    
    left = 0
    can_see_left = None
    for i3 in range(i1-1, -1, -1):
        if i3 == -1:
            break
        
        x2 = i3 - 1
        y2 = buildings[i3]
        gradient_left = gradient(x1, y1, x2, y2)
        
        if can_see_left is None or can_see_left > gradient_left:
            can_see_left = gradient_left
            left += 1
    
    if (right + left) > result:
        result = right + left
    
print(result)