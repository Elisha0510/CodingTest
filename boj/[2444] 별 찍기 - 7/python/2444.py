num = int(input())
number = (2*num)-1
list = []

for i in range(1, number, 2):
    side = (2*num-1-i)//2
    str = ''
    for x in range(side):
        str += ' '
    for x in range(i):
        str += '*'
    list.append(str)

str = ''
for i in range(number):
    str += '*'
list.append(str)

for i in range(number-2, 0, -2):
    side = (number - i)//2
    str = ''
    for x in range(side):
        str += ' '
    for x in range(i):
        str += '*'
    list.append(str)

for i in list:
    print(i)