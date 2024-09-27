import sys
from collections import deque

arr = list(map(int, sys.stdin.readline().strip().split()))

queue = []
for i in range(1, arr[0]+1):
    queue.append(i)

answer = []
p = 0
while 1:
    if len(queue) == 0:
        break
    p = (p + (arr[1] - 1)) % len(queue)
    answer.append(queue[p])
    queue.pop(p)

print("<", end="")
for i in range(len(answer)-1):
    print(f"{answer[i]}, ", end="")
print(f"{answer[-1]}>")

