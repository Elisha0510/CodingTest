from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort(reverse=True)
    dq = deque(people)
    
    while(1):
        if(len(dq)>=2):
            if(dq[0] + dq[-1] <= limit):
                cnt+=1
                dq.popleft()
                dq.pop()
            else: 
                cnt+=1
                dq.popleft() 
        elif(len(dq) == 1):
            cnt += 1
            break
        elif(len(dq) == 0):
            break

    return cnt
        
    
