import sys

arr = list(map(int, sys.stdin.readline().strip().split()))

x, y = 0,0
if arr[0] and arr[1] and arr[2] and arr[3] and arr[4] and arr[5]:
    a = arr[0] * arr[3]
    b = arr[1] * arr[3]
    c = arr[2] * arr[3]
    d = arr[3] * arr[0]
    e = arr[4] * arr[0]
    f = arr[5] * arr[0] 

    y = (c - f) // (b - e)
    x = (c - (b*y)) // a
elif not arr[0] and arr[3]:
    y = arr[2] // arr[1]
    x = (arr[5] - arr[4]*y) // arr[3]
elif not arr[3] and arr[0]:
    y = arr[5] // arr[4]
    x = (arr[2] - arr[1]*y) // arr[0]
elif not arr[1] and arr[4]:
    x = arr[2] // arr[0]
    y = (arr[5] - arr[3]*x) // arr[4]
elif not arr[4] and arr[1]:
    x = arr[5] // arr[3]
    y = (arr[2] - arr[0]*x) // arr[1]

print(f"{x} {y}")

