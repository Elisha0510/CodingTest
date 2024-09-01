import sys

arr = list(map(int, sys.stdin.readline().strip().split()))
max_length = max(arr)
arr.remove(max_length)
sum_num = sum(arr)
if sum_num > max_length:
    print(sum_num + max_length)
else:
    print(sum_num + sum_num - 1)
