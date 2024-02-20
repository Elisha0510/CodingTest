def solution(k, tangerine):    
    result = {}
    for i in range(0,len(tangerine)):
        if tangerine[i] in result:
            result[tangerine[i]] += 1
        else:
            result[tangerine[i]] = 1

    list_arr = list(result.values())
    list_arr.sort(reverse=True)
    
    cnt = 0
    sum1 = 0
    for i in list_arr:
        sum1 += i
        cnt += 1
        if(sum1 >= k):
            break
    
    return cnt