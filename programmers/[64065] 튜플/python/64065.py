def solution(s):
    s = s[1:len(s)-1]
    s = s.replace('{', '').split('},')
    s = '/'.join(s).replace('}','')
    s = s.split('/')
    
    num = []
    for i in s:
        num.append(i.split(','))
    
    num = sorted(num, key=len)
    
    answer = []
    for y in range(len(num)):
        for x in range(len(num[y])):
            if(num[y][x] not in answer):
                answer.append(num[y][x])
        
    answer = [int(i) for i in answer]
    return answer
    
            
    
    