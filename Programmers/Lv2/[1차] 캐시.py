from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque()
    
    for city in cities:
        city = city.lower()
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            elif cacheSize == 0:
                pass
            else:
                if len(cache) > 0:
                    cache.popleft()
                    cache.append(city)
                else:
                    cache.append(city)
            answer += 5
            
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer