import math

def solution(n, words):
    idx = []
    
    flag = 0
    for i in range(len(words)-1):
        before = list(words[i])
        after = list(words[i+1])
        if(before[-1] != after[0]):
            idx.append(i+1)
    
    min_value = 100
    for i in range(len(words)):
        for x in range(i+1, len(words)):
            if(words[i] == words[x] and min_value > x):
                flag = 1
                min_value = x
                
    if(flag == 1): 
        idx.append(min_value)
    
    try:
        print(min(idx))
        if(len(idx) >= 1):
            return [((min(idx)) % n) + 1, math.ceil((min(idx)+1)/n)]
    except ValueError: return [0,0]