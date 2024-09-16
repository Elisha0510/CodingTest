import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))

arr2 = list(set(arr))
arr2.sort()

d = {}
for i in range(len(arr2)):
    d[arr2[i]] = i

for a in arr:
    print(d[a], end=" ")
        