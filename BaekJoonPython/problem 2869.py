# 시간초과 발생
import sys

a, b, v = list(map(int, sys.stdin.readline().split()))

d = (v - b) / (a - b)
print(int(d) if d == int(d) else int(d) + 1)



# a = list(map(int, input().split()))

# A = a[0]
# B = a[1]
# C = a[2]
# go = 0
# cnt = 1
# count = 1
 
# while True:
#     if go + A < C:2
#         go = (A - B) * count
#         count = count + 1
#         cnt = cnt + 1
#     else:
#         print(cnt)
#         break