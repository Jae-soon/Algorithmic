def solution(genres, plays):
    answer = []
    
    genre_play_time = {}
    play_time = {}
    play_num = {}
    genre_count = {}
    
    for idx, genre in enumerate(genres):
        genre_play_time[genre] = 0
        genre_count[genre] = 0
        play_time[genre + "/" + str(idx)] = 0
    
    for idx, genre in enumerate(genres):
        genre_play_time[genre] += plays[idx]
        play_time[genre + "/" + str(idx)] += plays[idx]
        
    genre_play_time = sorted(genre_play_time.items(), key = lambda item:item[1], reverse=True)
    play_time = sorted(play_time.items(), key= lambda item:item[1], reverse=True)
    sort_play_time = []
    
    for i in play_time:
        if genre_count[i[0].split("/")[0]] >= 2:
            continue
        sort_play_time.append(i)
        genre_count[i[0].split("/")[0]] += 1
    
    for i in genre_play_time:
        for j in sort_play_time:
            if i[0] in j[0].split("/"):
                answer.append(int(j[0].split("/")[1]))
    
    return answer