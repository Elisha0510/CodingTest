import sys

def gcd(a, b):
    c = -1
    while 1:
        c = a % b
        if not c:
            return b
        a = b
        b = c

arr = list(map(int, sys.stdin.readline().strip().split()))
arr2 = list(map(int, sys.stdin.readline().strip().split()))

number = 0
if arr2[1] >= arr[1]:
    number = gcd(arr2[1], arr[1])
else:
    number = gcd(arr[1], arr2[1])

denom = arr[1] * arr2[1] // number
num = (denom // arr[1]) * arr[0] + (denom // arr2[1]) * arr2[0]

number2 = gcd(denom, num)

print(f"{num//number2} {denom//number2}")
