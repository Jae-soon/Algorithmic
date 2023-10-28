def solution(n, words):
    answer = [0, 0]
    temp = [words[0]]

    for i in range(1, len(words)):
        if words[i][0] != temp[-1][-1] or words[i] in temp:
            return [i%n + 1, i // n + 1]
        
        temp.append(words[i])
        
    return answer