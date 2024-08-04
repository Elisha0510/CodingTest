a = int(input())

div = 2
while a != 1:
    if a % div == 0:
        print(div)
        a = a // div
    else:
        div += 1
    