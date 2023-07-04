from collections import deque

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()

    # 2단계
    accept_words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", "_", ".", "1", "2", "3", "4", "5", "6", "7", "8" ,"9", "0"]
    for word in new_id:
        if word not in accept_words:
            new_id = new_id.replace(word, "")
    
    # 3단계
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    # 4단계
    def _4th(new_id):
        while new_id[0] == "." or new_id[-1] == ".": 
            if new_id[0] == ".":
                new_id = new_id[1:]
            elif new_id[-1] == ".":
                new_id = new_id[:len(new_id) - 1]

            if len(new_id) == 0:
                break
        
        return new_id
    new_id = _4th(new_id)
    
    # 5단계
    if len(new_id) == 0:
        new_id += "a"
        
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
        new_id = _4th(new_id)
    
    # 7단계
    if len(new_id) <= 2:
        for _ in range(3 - len(new_id)):
            new_id += new_id[-1]

    return new_id