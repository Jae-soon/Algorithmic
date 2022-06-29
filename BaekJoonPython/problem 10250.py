T = int(input())

for _ in range(T):
    H, W, guest = list(map(int, input().split()))
    YY = guest % H
    XX = (guest // H) + 1
    
    if YY == 0:
        XX = XX - 1
        YY = H
    
    print(YY * 100 + XX) 