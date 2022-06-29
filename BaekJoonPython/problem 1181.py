import sys

inf = sys.stdin
N = inf.readline()

word_li = list()

for _ in range(int(N)):
    word_li.append(input())

set_word = list(set(word_li))
set_word.sort()
set_word.sort(key=len)

for i in set_word:
    print(i)