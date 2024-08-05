l = []
for i in range(3):
    l.append(int(input()))

all = l[0] + l[1] + l[2]

flag = 0
for i in range(3):
    if l.count(l[i]) == 2:
        flag = 1
        break

if all != 180:
    print('Error')
elif l[0] == 60 and l[1] == 60 and l[2] == 60:
    print('Equilateral')
elif all == 180 and flag:
    print('Isosceles')
elif all == 180 and not flag:
    print('Scalene')