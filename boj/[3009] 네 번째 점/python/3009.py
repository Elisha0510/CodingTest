import sys 

x = []
y = []
for i in range(3):
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    x.append(l[0])
    y.append(l[1])

x_set = list(set(x))
y_set = list(set(y))


answer = []
for e in x_set:
    if x.count(e) == 1:
        answer.append(e)

for e in y_set:
    if y.count(e) == 1:
        answer.append(e)

print(f'{answer[0]} {answer[1]}')
