num = int(input())

cnt = 1
while num > 0:
    pre = num
    num -= cnt
    cnt += 1

if cnt % 2:
    print(f'{1 + (pre - 1)}/{(cnt- 1) - (pre - 1)}')
else:
    print(f'{(cnt - 1) - (pre - 1)}/{1 + (pre - 1)}')