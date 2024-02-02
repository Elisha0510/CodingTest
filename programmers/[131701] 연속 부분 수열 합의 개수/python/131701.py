def solution(elements):

    num = len(elements)
    sum_cnt = 0
    # 길이 1
    result = list(set(elements))
    # 길이 최대
    for x in range(num):
        sum_cnt += elements[x]
    result.append(sum_cnt)
    
    arr = elements + elements
        
    a = 2
    while(1):
        if(a == len(elements)):
            break
        for i in range(len(elements)):
            result.append(sum(arr[i:i+a]))
        a += 1
    
    return len(list(set(result)))          
                