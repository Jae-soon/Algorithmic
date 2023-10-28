def solution(s):
    stack = []

    for i in s:
        if stack and stack[-1] == i: # stack에 쌓여있고, 스택의 숫자와 같다면
            stack.pop() # 스택에서 제거
            continue

        stack.append(i)
    
    return int(not stack) # 스택이 비어있다면 1, 있다면 0 반환