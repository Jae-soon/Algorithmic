import sys

all_list = []

for _ in range(9):
    all_list.append(list(map(int, sys.stdin.readline().split())))

x = 0
y = 0
max = -1

for i in range(9):
    for j in range(9):
        if all_list[i][j] > max:
            max = all_list[i][j]
            x = i + 1
            y = j + 1
        
print(max)
print(x, y)