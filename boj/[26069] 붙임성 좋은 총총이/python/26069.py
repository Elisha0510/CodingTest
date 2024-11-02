import sys

n = int(input())
name = []
flag = 0
dance = ''
for i in range(n):
    arr = list(sys.stdin.readline().split())
    if flag and (arr[0] in name or arr[1] in name):
        name.append(arr[0])
        name.append(arr[1])
    if arr[0] == "ChongChong" or arr[1] == "ChongChong":
        name.append(arr[0])
        name.append(arr[1])
        flag = 1

set_name = list(set(name))
print(len(set_name))