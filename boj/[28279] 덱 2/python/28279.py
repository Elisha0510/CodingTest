import sys
from collections import deque

n = int(sys.stdin.readline().strip())

d = deque()
for i in range(n):
    arr = sys.stdin.readline().strip().split()
    if arr[0] == '1':
        d.appendleft(int(arr[1]))
    elif arr[0] == '2':
        d.append(int(arr[1]))
    elif arr[0] == '3':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.popleft()
    elif arr[0] == '4':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            d.pop()
    elif arr[0] == '5':
        print(len(d))
    elif arr[0] == '6':
        print(int(not len(d)))
    elif arr[0] == '7':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif arr[0] == '8':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])