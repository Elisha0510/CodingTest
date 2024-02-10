def solution(cacheSize, cities):
    cache = []
    time = 0
    cities = [i.lower() for i in cities]
    for i in range(0, len(cities)):
        if cities[i] in cache:
            time += 1
            cache.remove(cities[i])
        else:
            time += 5
        cache.append(cities[i])
        if(len(cache) > cacheSize):
            cache = cache[1: 1+cacheSize]
        
    return time
    
    