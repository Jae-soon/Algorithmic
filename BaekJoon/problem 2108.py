import sys

inf = sys.stdin
N = int(inf.readline())
num_li = list()

for _ in range(N):
    num = int(inf.readline())
    num_li.append(num)

num_li.sort()

# 산술평균
mean = round(sum(num_li)/N)
print(mean)
# 중앙값
center = num_li[int((N-1)/2)]
print(center)
# 최빈값
counts = dict()
for i in range(1, N+1):
    counts[i] = []

max_count = 1
count = 1
for j in range(1, N):
    if num_li[j] == num_li[j]:
        count += 1
    else:
        counts[count].append(num_li[j - 1])
        if max_count < count:
            max_count = count
            count = 1
    if j == N - 1:
        counts[count].append(num_li[j])
        if max_count < count:
            max_count = count

if N == 1:
    counts[1].append(num_li[0])

counts[max_count].sort()
if len(counts[max_count]) == 1:
    print(counts[max_count][0])
else:
    print(counts[max_count][1])
# 범위
max_num = max(num_li)
min_num = min(num_li)
min_max_range = max_num - min_num
print(min_max_range)