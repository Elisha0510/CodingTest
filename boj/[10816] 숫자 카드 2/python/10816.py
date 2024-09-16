import sys

n = int(sys.stdin.readline().strip())
arr_1 = list(map(int, sys.stdin.readline().strip().split()))

num = int(sys.stdin.readline().strip())
arr_2 = list(map(int, sys.stdin.readline().strip().split()))

d = {}
for a in arr_1:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

for a in arr_2:
    if a in d:
        print(d[a], end = " ")
    else:
        print(0, end=" ")