def solution(genres, plays):
    answer = []
    play_dict = {}
    count_di = {}
    genre_di = {}
    sort_genres = sorted(genres)

    for i in sort_genres:
        genre_di[i] = []
        count_di[i] = 0
    
    for i, g in enumerate(genres):
        count_di[g] += plays[i]
        genre_di[g].append([i, plays[i]])

    for i 

    max_count_genre = max(count_di, key=count_di.get)

    for k, v in genre_di.items():
        count_li = []
        if k == max_count_genre:
            
            answer.append(genre_di[k])

    print(count_di)
    print(genre_di)


    # 값 채워넣기
    for i, g in enumerate(genres):
        key = g + str(i)
        play_dict[key] = plays[i]
    
    # for k, v in play_dict.items():
    #     if k[0, -1] in sort_genres:
            

    return answer