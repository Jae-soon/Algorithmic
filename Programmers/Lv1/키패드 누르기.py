def solution(numbers, hand):
    answer = ''
    pad = {1:[0, 0], 2:[0, 1], 3:[0, 2], 4:[1, 0], 5:[1, 1], 6:[1, 2], 7:[2, 0], 8:[2, 1], 9:[2, 2], "*":[3, 0], 0:[3, 1], "#":[3, 2]}

    l_now = pad["*"] # [1, 0]
    r_now = pad["#"] # [0, 2]

    for i in numbers:
        now = pad[i] # [1, 1]
        if i in [1, 4, 7]:
            answer += "L"
            l_now = now
        elif i in [3, 6, 9]:
            answer += "R"
            r_now = now
        else:
            left = 0
            right = 0
            
            for a, b, c in zip(l_now, r_now, now):
                left += abs(a-c)
                right += abs(b-c)
            
            if left < right:
                answer += "L"
                l_now = now
            
            elif right < left:
                answer += "R"
                r_now = now

            else:
                if hand == "left":
                    answer += "L"
                    l_now = now
                else:
                    answer += "R"
                    r_now = now

    return answer