answer = []

def findKeyWord(history, keyword):
    for sentence in history:
        words = list(sentence.split())
        for word in words:
            if word == keyword:
                answer.append(sentence)

def findSentence(history, keyword):
    for sentence in history:
        if keyword in sentence:
            answer.append(sentence)


def solution(history, option, keyword):
    
    if option:
        if option[0][0] == "W" and option[0][1] == "T":
            findKeyWord(history, keyword)
        else:
            findSentence(history, keyword)
    else:
        findSentence(history, keyword)
    
    if not answer:
        answer.append("empty")

    return answer


history = ["hello i am david", "hello kail", "hi tina"]
option = [["",""]]
keyword = "i"
print(solution(history, option, keyword))