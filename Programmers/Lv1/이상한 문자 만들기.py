def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        ans = ""
        for i, val in enumerate(word):
            if i % 2 == 1:
                ans += val.lower()
            else:
                ans += val.upper()
        answer.append(ans)
    # answer = answer.strip()
    return " ".join(answer)