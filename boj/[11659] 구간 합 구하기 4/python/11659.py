import sys
input = sys.stdin.readline

a, b = map(int, input().split(' '))
num_arr = list(map(int, input().split(' ')))

num = 0
sum_arr = [0]
for i in range(len(num_arr)):
    num = num + num_arr[i]
    sum_arr.append(num)

for i in range(b):
    c, d = map(int, input().split(' '))
    print(sum_arr[d] - sum_arr[c-1])