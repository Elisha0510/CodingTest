import sys

n = int(sys.stdin.readline().strip())

answer = []
flag = 0
a = []
for i in range(n):
    string = sys.stdin.readline().strip()
    if string == "ENTER":
        answer.append(a)
        a = []
    else:
        a.append(string)
    if i == n - 1:
        answer.append(a)
    
sum = 0
for aw in answer:
    sum += len(list(set(aw)))

print(sum)