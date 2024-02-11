import math

def solution(progresses, speeds):
    
    date = []
    for i in range(len(progresses)):
        date.append(math.ceil((100-progresses[i]) / speeds[i]))
    
    max = date[0]
    cnt = 0
    answer = []
    for i in range(len(date)):
        if(max < date[i]):
            answer.append(cnt)
            max = date[i]
            cnt = 1
        else:
            cnt += 1
        if(i == len(date)-1):
            answer.append(cnt)
    
    return answer