import sys

n = int(sys.stdin.readline())
dic = [0] * 10

for i in range(1, n + 1):
    num_li = list(str(i))
    for j in num_li:
        dic[int(j)] += 1

for i in dic:
    print(i, end=" ")
# while n != 0:
#     while n % 10 != 9:
#         for i in str(n):
#             num_list[int(i)] += point
#         n -= 1
#     if n < 10:
#         for i in range(n+1):
#             num_list[i] += point
#         num_list[0] -= point
#         break
#     else:
#         for i in range(10):
#             num_list[i] += (n // 10 + 1) * point
#     num_list[0] -= point
#     point *= 10
#     n //= 10

# for i in num_list:
#     print(i, end=" ")