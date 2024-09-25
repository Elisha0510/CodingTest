import sys
from collections import deque

n = int(sys.stdin.readline().strip())

queue = deque()
for i in range(n):
    l = sys.stdin.readline().strip().split()
    if l[0] == "push":
        queue.append(int(l[1]))
    elif l[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif l[0] == "size":
        print(len(queue))
    elif l[0] == "empty":
        print(int(not len(queue)))
    elif l[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif l[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])