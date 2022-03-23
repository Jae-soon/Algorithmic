"""
N개의 과목만큼 입력을 받음
sort 후 뒷쪽부터 K개만큼 더함
"""

import sys

inf = sys.stdin 

T = inf.readline();

for t in range(0, int(T)):
    
    Answer=0;

    a = list(map(int, input().split()))
    N = a[0]
    K = a[1]
    score_list = list(map(int, input().split()))

    score_list.sort()
    
    for i in range(K):
        Answer = Answer + score_list[N - i - 1]    
	
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close() 