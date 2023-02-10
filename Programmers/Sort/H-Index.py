def solution(citations):
    answer = 0
    sort_citations = sorted(citations, reverse=True)

    for i in range(len(citations)):
        if i + 1 <= sort_citations[i]:
            answer = i + 1
        else:
            return answer

    return answer
