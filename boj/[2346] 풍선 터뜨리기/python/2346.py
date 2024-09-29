import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

num = []
for i in range(n):
    num.append(i+1)

p = 0
for i in range(n):
    print(num[p], end = " ")
    next = arr[p]
    arr.pop(p)
    num.pop(p)
    if len(arr) == 0:
        break
    if next > 0:
        p = (p + next -1) % len(arr)
    else:
        p = (p + next) % len(arr)
    