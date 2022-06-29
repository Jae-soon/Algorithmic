import sys

inf = sys.stdin
N = int(inf.readline())
num_li = list()

for i in str(N):
    num_li.append(int(i))
    
num_li.sort(reverse=True)

for i in num_li:
    print(i, end='')
