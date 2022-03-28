import sys
import math

#inf = open('input.txt');
inf = sys.stdin 

T = inf.readline();

for t in range(0, int(T)):
    
    Answer=0;
    
	#############################################################################################
    score = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
    
    A, B, C, D, E = map(int, input().split()) # BULL, TRIPLE시작, TRIPLE 종료, DOUBLE시작, DOUBLE 종료
    N = int(input())
    sum = 0
    for i in range(N):
        x, y = map(int, input().split()) # x, y값 입력
        dist = math.sqrt(x*x + y*y) # 다트와 원점 거리

        if dist < A: # Bull일 경우
            sum += 50
        elif dist > E: # out Board일 경우
            continue
        else:
            radian = math.atan2(y, x) 
            angle = radian * 180 / math.pi
            angle += 180
            
            angle %= 360

            s = score[int(angle/18)]
            if B < dist and dist < C:
                sum += s * 3
            elif D < dist and dist < E:
                sum += s * 2
            elif E < dist:
                sum += 0
            else:
                sum += s
	#############################################################################################
	
	# Print the answer to standard output(screen).
    print('Case #%d' %(int(t)+1))    
    print(sum)
inf.close()