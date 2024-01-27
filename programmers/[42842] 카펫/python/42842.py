def solution(brown, yellow):  
    pair = []
    for i in range(1,yellow+1):
        if(yellow % i == 0):
            pair.append(i)
            
    print(pair)
    
    result = []
    for i in range(0, int(len(pair)/2+1)):
        if(len(pair) == 1):
            sum = pair[0]*2+2*(2+pair[0])
        else:
            sum = pair[-1]*2+2*(2+pair[0])
            
        if(brown == sum):
            result.append(pair[-1]+2)
            result.append(pair[0]+2)
            print(result)
            break
        else:
            pair.pop()
            pair.pop(0)
    
    return result
        
        
            
