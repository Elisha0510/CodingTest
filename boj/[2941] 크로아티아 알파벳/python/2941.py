list = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

a = input()

cnt = 0
for i in list:
    result = a.count(i)
    if(result):
        for x in range(result):
            a = a.replace(i, "1")

print(len(a))