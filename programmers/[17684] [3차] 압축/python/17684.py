def solution(msg):
    dic = {}
    for i in range(65, 91):
        dic[chr(i)] = i - 64
    
    length = len(dic)
    
    cnt = 1
    answer = []
    i = 0
    flag = 0
    while(i <= len(msg)):
        for x in range(cnt+1, 0, -1):
            if msg[i:i+x] in dic.keys():
                answer.append(dic[msg[i:i+x]])
                if(i != len(msg)-2):
                    string = msg[i:i+x] + msg[i+x: i+x+1]
                cnt += 1
                length += 1
                flag=1
                dic[string] = length
                break
        if flag:
            i += x
        else:
            i += 1

    return answer