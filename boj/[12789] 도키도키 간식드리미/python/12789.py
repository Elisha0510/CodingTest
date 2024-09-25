import sys

stack = []

n = int(sys.stdin.readline().strip())
queue = list(map(int, sys.stdin.readline().strip().split()))

num = 1
flag = 0
while 1:
    if len(queue) == 0 and len(stack) == 0:
        flag = 1
        break
    if len(queue) == 0:
        if stack[-1] == num:
            stack.pop()
            num += 1
        else:
            break
    elif queue[0] == num:
        queue.pop(0)
        num += 1
    else: 
        if len(stack) and stack[-1] == num:
            stack.pop()
            num += 1
        else:
            stack.append(queue[0])
            queue.pop(0)

if flag:
    print("Nice")
else:
    print("Sad")