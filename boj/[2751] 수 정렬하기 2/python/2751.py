import sys

n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    arr.append(num)

arr.sort()

for i in range(n):
    print(arr[i])