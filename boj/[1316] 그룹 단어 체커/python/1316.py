import sys

num = int(input())

cnt = 0
for i in range(num):
    str = sys.stdin.readline()
    dict = {}
    for x in range(0, len(str)):
        if str[x] not in dict:
            dict[str[x]] = x
        else:
            pre = dict[str[x]]
            comp = pre + 1
            if comp == x:
                dict[str[x]] = x
            else:
                cnt += 1
                break

print(num - cnt)
