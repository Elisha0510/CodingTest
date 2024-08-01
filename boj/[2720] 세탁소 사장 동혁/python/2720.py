import sys

num = int(input())

answer = []
for n in range(num):
    money = int(sys.stdin.readline().rstrip())

    arr = []
    div = [25,10,5,1]
    for d in div:
        arr.append(money//d)
        money = money % d
    answer.append(arr)

for a in answer:
    print(' '.join([str(b) for b in a]))