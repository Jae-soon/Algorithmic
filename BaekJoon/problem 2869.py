# 시간초과 발생

A, B, C = list(map(int, input().split()))
count = 1

while True:
    C = C - A
    if C <= 0:
        print(count)
        break
    C = C + B
    count = count + 1

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