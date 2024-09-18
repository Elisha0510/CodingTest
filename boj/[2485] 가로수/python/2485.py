import sys

n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr2 = []
for i in range(1, len(arr)):
    arr2.append(arr[i] - arr[i-1])

arr2.sort()

def gcd(a, b):
    c = -1
    while 1:
        c = a % b
        if not c:
            return b
        a = b
        b = c

for i in range(1, len(arr2)):
    arr2[i] = gcd(arr2[i], arr2[i-1])

length = arr[-1] - arr[0]
print(length // arr2[-1] + 1 - len(arr))