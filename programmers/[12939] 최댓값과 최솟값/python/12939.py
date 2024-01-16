def solution(s):
    list_str = list(map(int,s.split(' ')))
    print(list_str)
    
    max = -9999
    for i in list_str:
        if(max <= i):
            max = i
            
    min = 9999
    for i in list_str:
        if(min >= i):
            min = i
    
    result = str(min)+" "+str(max)
    return result
        
    
    