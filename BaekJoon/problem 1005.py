import sys
from collections import deque

inf = sys.stdin
t = inf.readline()

for _ in range(int(t)):
    n, k = map(int, input().split())
    time = list(map(int, inf.readline().split()))
    seq = [[] for _ in range(n+1)]
    inDegree = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]

    for _ in range(k):
        a, b = map(int, inf.readline().split())
        seq[a].append(b)
        inDegree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        a = q.popleft()
        for i in seq[a]:
            inDegree[i] -= 1
            dp[i] = max(dp[a] + time[i], dp[i])
            if inDegree[i] == 0:
                q.append(i)
    
    ans = int(inf.readline())
    print(dp[ans])
