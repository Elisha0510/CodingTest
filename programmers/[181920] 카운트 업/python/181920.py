def solution(start_num, end_num):
    answer = [0 for i in range(start_num, end_num+1)]
    
    for i in range(start_num, end_num+1):
        answer[i-start_num] = i
        
    return answer