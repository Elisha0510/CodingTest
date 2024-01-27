def solution(brown, yellow): 
    
    sum = brown + yellow
    
    for i in range(1, sum+1):
        if(sum % i == 0 and yellow == (i-2)*(int(sum/i)-2)):
            return [int(sum/i), i]
        
        
            
