def solution(clothes):
    arr = []
    for i in clothes:
        arr.append(i[1])
    type = list(set(arr))
    
    dic = {}
    cnt = 0
    for x in arr:
        for i in clothes:
            if(i[1] == x):
                cnt += 1
        
        dic[x] = cnt
        cnt = 0

    val = dic.values()
    mul = 1
    for i in val:
        mul *= (i+1)
    
    return mul - 1
    
    
    
    
    