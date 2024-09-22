import sys

max_number = 1000001
arr = list(True for _ in range(max_number))
arr[0] = False
arr[1] = False

for i in range(2, max_number):
    if arr[i]:
        for j in range(2*i, max_number, i):
            arr[j] = False

n = int(sys.stdin.readline().strip())

for i in range(n):
    number = int(sys.stdin.readline().strip())

    cnt = 0
    for i in range(2, number // 2 + 1):
        if arr[i] and arr[number - i]:
            cnt += 1

    print(cnt)

