def solution(citations):
    answer = 0
    max_num = max(citations)
    for i in range(max_num+1):
        a = list(map(lambda x: x>=i, citations))
        if(a.count(True) >= i):
            answer = i
    
    return answer