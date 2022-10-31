import sys


n = sys.stdin.readline()

num_list = list(map(int, sys.stdin.readline().split(" ")))

v = sys.stdin.readline()

count = 0

for i in num_list:
    if(int(v) == i):
        count += 1

print(count)