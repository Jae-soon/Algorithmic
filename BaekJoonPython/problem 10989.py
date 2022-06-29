import sys

N = int(sys.stdin.readline())
num = [0] * 10001

for _ in range(N):
    a = int(sys.stdin.readline()) # a = 1
    num[a] = num[a] + 1 # num[1] = 0 + 1

for i in range(10001): # i = 1
    if num[i] != 0: #num[1] = 1
        for _ in range(num[i]): #
            print(i) # 1
