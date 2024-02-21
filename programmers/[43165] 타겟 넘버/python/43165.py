def solution(numbers, target):
    answer = []
    def dfs(num, cnt):
        if(num == target and cnt == len(numbers)):
            answer.append(1)
            return
        elif(num != target and cnt == len(numbers)):
            return
        dfs(num + numbers[cnt], cnt+1)
        dfs(num - numbers[cnt], cnt+1)
    
    dfs(numbers[0], 1)
    dfs(-1 * numbers[0], 1)
    
    return len(answer)