def solution(want, number, discount):
    sum_num = sum(number)
    repeat = len(discount) - sum_num + 1
    
    answer = 0
    for i in range(repeat):
        cnt = 0
        arr = discount[i:i+10]
        for x in range(len(want)):
            result = arr.count(want[x])
            if(result >= number[x]):
                cnt += 1
        if(cnt == len(number)):
            answer += 1
    
    return answer
        