n = int(input())

start_num = 666
cnt = 0
while 1:
    if '666' in str(start_num):
        cnt += 1
    if cnt == n:
        break
    start_num += 1

print(start_num)