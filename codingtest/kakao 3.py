def solution(s, times):
    answer = []
    day_list = []
    s_day, s_hour, s_min, s_sec = map(int, s.split(":")[2:])
    day_list.append(s_day)

    new_day = s_day
    new_hour = s_hour
    new_min = s_min
    new_sec = s_sec
    result = 0
    count = 0

    for time in times:
        day, hour, minute, sec = map(int, time.split(":"))
        new_day += day

        if new_sec + sec >= 60:
            new_min += 1
            new_sec -= 60

        new_sec += sec

        if new_min + minute >= 60:
            new_hour += 1
            new_min -= 60

        new_min += minute
        
        if new_hour + hour >= 24:
            new_day += 1
            new_hour -= 24

        new_hour += hour

        day_list.append(new_day)

    for _ in range(int(min(day_list)), int(max(day_list)) + 1):
        count += 1
    
    set_list = set(day_list)

    if count == len(set_list):
        result = 1

    answer.append(result)
    answer.append(count)


    return answer


s = "2021:04:12:16:08:35"
times = ["01:06:30:00", "01:01:12:00", "00:00:09:25"]
print(solution(s, times))