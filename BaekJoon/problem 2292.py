# 반복되는 구간 찾아보기

num = int(input())

start = 1
result = 1
while num > start:
    start += 6 * result
    result += 1
print(result)