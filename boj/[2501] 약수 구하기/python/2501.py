import sys

a = list(map(int, sys.stdin.readline().rstrip().split()))

arr = []
for i in range(1,a[0]+1):
    if a[0] % i == 0:
        arr.append(i)

if len(arr) >= a[1]:
    print(arr[a[1]-1])
else:
    print(0)