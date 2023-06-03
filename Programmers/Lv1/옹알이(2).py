from itertools import permutations

def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    repeats = ["ayaaya", "yeye", "woowoo", "mama"]

    for x in babbling:
        for word in repeats:
            x = x.replace(word, "X")
        for word in baby:
            x = x.replace(word, "O")

        isValid = True
        for char in x:
            if char != "O":
                isValid = False
        
        if isValid:
            answer += 1
        
    return answer