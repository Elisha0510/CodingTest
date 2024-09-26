import sys
from collections import deque
queue = deque()

n = int(sys.stdin.readline().strip())

for i in range(1, n+1):
    queue.append(i)

while 1:
    if len(queue) == 1:
        break
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())

print(queue.popleft())