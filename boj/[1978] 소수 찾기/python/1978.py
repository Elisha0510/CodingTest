import sys

num = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for a in arr:
    if a == 1:
        cnt += 1
    flag = 0
    for n in range(2,a):
        if a % n == 0:
            flag = 1
            break
    if flag:
        cnt += 1

print(len(arr) - cnt)
