import sys

inf = sys.stdin 

T = inf.readline();

for t in range(0, int(T)):
    
    Answer=0;
    N = int(input())
    if N < 3000000:
        num = list(map(int, input().split()))
        Answer = num[0]
        for n in range(1, len(num)):
            Answer = Answer^num[n]
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close() 