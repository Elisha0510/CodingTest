a = int(input())
b = int(input())

if a == 1:
    a += 1
if a == 1 and b == 1:
    print(-1)

answer = []
for i in range(a, b+1):
    flag = 0
    for n in range(2, i):
        if i % n == 0:
            flag = 1
            break
    if not flag:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))