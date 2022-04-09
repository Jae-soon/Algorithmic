import sys

inf = sys.stdin
n, m = map(int, inf.readline().split())
location = list(map(int, inf.readline().split()))

q = [i for i in range(1, n + 1)]
count = 0

for i in range(m):
    q_len = len(q)
    q_index = q.index(location[i])
    
    if q_index < q_len - q_index:
        while 1:
            if q[0] == location[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                count += 1
    else:
        while 1:
            if q[0] == location[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                count += 1
print(count)