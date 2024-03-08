a = int(input())
old = input().split(' ')

old = [int(x) for x in old]

max_num = int(max(old))

new = []
for i in range(a):
    new.append((int(old[i])/max_num)*100)

print(sum(new)/a)