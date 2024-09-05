num = int(input())

answer = []

i = 0
n = num
while 1:
    cnt = 0
    n = num
    cnt += i
    n -= (5*i)
    if n < 0:
        break
    if n % 3 == 0:
        cnt += n // 3
        answer.append(cnt)
    i += 1

if len(answer):
    print(min(answer))
else:
    print(-1)