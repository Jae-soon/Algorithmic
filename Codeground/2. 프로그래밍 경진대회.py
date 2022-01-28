import sys

inf = sys.stdin 

T = inf.readline();

for t in range(0, int(T)):
    
    Answer=0;
    N = inf.readline()
    score_list = list()
    max_list = list()
    for _ in range(int(N)):
        score = int(input())
        score_list.append(score)

    score_list.sort(reverse=True) # 7 6 5 3 1
    for n in range(len(score_list)):
        max_list.append(score_list[n] + n + 1) # 8 8 8 7 6
    
    max = max(max_list) # 8 
    for n in range(len(max_list)):
        if max_list[n] >= max:
            Answer = Answer + 1
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close()