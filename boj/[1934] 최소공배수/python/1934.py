import sys

def gcd(a, b):
    c = -1
    while 1:
        c = a % b
        if not c:
            return b
        a = b
        b = c

n = int(sys.stdin.readline().strip())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    if arr[0] >= arr[1]:
        number = gcd(arr[0], arr[1])
    else:
        number = gcd(arr[1], arr[0])
    
    print(arr[0]*arr[1]//number)