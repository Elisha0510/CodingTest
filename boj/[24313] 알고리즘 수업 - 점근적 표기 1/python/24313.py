import sys

arr = list(map(int, sys.stdin.readline().strip().split()))
g = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

flag = 0
for i in range(c, 101):

    f = arr[0] * i + arr[1]

    cg = i * g

    if f > cg:
        flag = 1
        break

if flag:
    print(0)
else:
    print(1)
