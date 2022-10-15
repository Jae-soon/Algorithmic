import sys

n, m = map(int, sys.stdin.readline().split())
s_list = list()
s__list = list()
count = 0

for _ in range(n):
    s_word = sys.stdin.readline()
    s_list.append(s_word)
    
for _ in range(m):
    word = sys.stdin.readline()
    
    if word in s_list:
        count += 1

print(count)
