import sys

num_arr = list(map(int, sys.stdin.readline().strip().split()))

d = {}
for n in range(num_arr[0]):
    s = sys.stdin.readline().strip()
    d[s] = 0

cnt = 0
for n in range(num_arr[1]):
    s = sys.stdin.readline().strip()
    if s in d:
        cnt += 1

print(cnt)