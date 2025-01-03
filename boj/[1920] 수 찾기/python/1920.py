import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().strip().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().strip().split()))

arr.sort()
for a in arr2:
    start = 0
    end = len(arr) - 1
    exist = False

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == a:
            exist = True
            print(1)
            break
        elif arr[mid] > a:
            end = mid - 1
        else:
            start = mid + 1

    if not exist:
        print(0)

        