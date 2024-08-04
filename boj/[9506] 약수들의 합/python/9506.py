import sys

arr = []
while 1:
    a = int(sys.stdin.readline().rstrip())
    if a == -1:
        break
    arr.append(a)

answer = []
for a in arr:
    l = []
    for i in range(1, a):
        if a % i == 0:
            l.append(i)
    if sum(l) == a:       
        answer.append(l)
    else:
        answer.append([])

for i in range(len(answer)):
    if len(answer[i]) == 0:
        print(f'{arr[i]} is NOT perfect.')
    else:
        print(f'{arr[i]} = {answer[i][0]} ', end='')
        for idx in range(1, len(answer[i])):
            if idx == len(answer[i]) - 1:
                print(f'+ {answer[i][idx]} ')
            else:
                print(f'+ {answer[i][idx]} ', end='')
