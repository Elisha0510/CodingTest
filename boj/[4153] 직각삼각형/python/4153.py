import sys

while(1):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    if arr == [0,0,0]:
        break
    arr.sort()
    p = arr[0]**2 + arr[1]**2
    if arr[2]**2 == p:
        print("right")
    else:
        print("wrong")
