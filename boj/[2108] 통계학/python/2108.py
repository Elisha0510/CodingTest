import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

print(round(sum(arr)/n))

arr.sort()
print(arr[int(n/2)])

d = {}
for i in range(n):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

d = sorted(d.items(), key=lambda x:x[1], reverse=True)
max_num = d[0][1]
arr_num = []
for d_element in d:
    if d_element[1] == max_num:
        arr_num.append(d_element[0])

arr_num.sort()
if len(arr_num)> 1:
    print(arr_num[1])
else:
    print(arr_num[0])

print(arr[-1] - arr[0])