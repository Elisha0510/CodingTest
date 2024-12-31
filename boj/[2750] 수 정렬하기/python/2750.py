import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

for i in range(n-1):
    for j in range((n-1)-i):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp

for a in arr:
    print(a)
    