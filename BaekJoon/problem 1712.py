cost = list(map(int, input().split()))

A = cost[0]
B = cost[1]
C = cost[2]
x = 0
total_cost = A + B * x
sell_cost = C * x

if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1))