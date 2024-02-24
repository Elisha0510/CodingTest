def solution(numbers):
    answer = [-1 for x in range(len(numbers))]
    stack = []
    stack.append(0)
    
    i=1
    while(i < len(numbers)):
        if(len(stack) != 0 and numbers[stack[-1]] < numbers[i]):
            answer[stack[-1]] = numbers[i]
            stack.pop()
        elif(len(stack) == 0 or numbers[stack[-1] >= numbers[i]]):
            stack.append(i)
            i += 1
    return answer