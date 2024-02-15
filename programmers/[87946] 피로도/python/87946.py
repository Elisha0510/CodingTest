from itertools import permutations

def solution(k, dungeons):
    cntArr = []
    cnt = 0
    caseArr = list(permutations(dungeons))
    
    for y in caseArr:
        kNum = k
        for x in y:
            if(kNum >= x[0] and kNum >= x[1]):
                kNum -= x[1]
                cnt += 1
        cntArr.append(cnt)
        cnt = 0
    
    return max(cntArr)
    
        
        