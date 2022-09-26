# 시간초과 발생

import sys

A, B, C = map(int, sys.stdin.readline().split())
count = 0
total = 0

while True:
    total += A # 2 3 4 5
    count += 1 # 1 
    if(total >= C):
        print(count)
        break
    total -= B
    
        

# while True: #n
#     C = C - A
#     if C <= 0:
#         print(count)
#         break
#     C = C + B
#     count = count + 1

# a = list(map(int, input().split()))

# A = a[0]
# B = a[1]
# C = a[2]
# go = 0
# cnt = 1
# count = 1
 
# while True:
#     if go + A < C:
#         go = (A - B) * count
#         count = count + 1
#         cnt = cnt + 1
#     else:
#         print(cnt)
#         break