import math

def solution(n):
    
    cnt = 0
    result = [{1:n, 2:0}]
    num = n
    for i in range(n):
        if(num >= 2):
            num -= 2
            cnt+=1
            result.append({1: num, 2: cnt})
        if(num == 0): break

    
    print(result)
    
    answer = 0
    for i in result:
        sum = i[1] + i[2]
        answer += math.comb(sum, i[1]) * math.comb(sum - i[1], sum - i[1])
        
    return answer % 1234567
            