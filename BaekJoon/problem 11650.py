import sys

inf = sys.stdin
N = inf.readline()

num_dic = dict()
li = list()
for _ in range(int(N)):
    li.append(list(map(int, inf.readline().split())))
li.sort(key=lambda x: (x[1], x[0]))

print(li)
for i in li:
    print(i[0], i[1])


