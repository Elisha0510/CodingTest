import heapq

def solution(scoville, K):
    i = 0
    heapq.heapify(scoville)
    
    while scoville:
        a = heapq.heappop(scoville)
        if(a >= K):
            break
        if(len(scoville) == 0):
            return -1
        b = heapq.heappop(scoville)
        result = a + 2*b
        heapq.heappush(scoville, result)
        i += 1
    
    return i