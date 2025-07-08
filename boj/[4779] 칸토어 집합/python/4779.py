import sys

def make_str(n):
    s = ''
    for a in range(3**n):
        s += '-'

    return s

def cantor_set(s):
    if s[0] == ' ':
        return s
    if s == '-' and len(s) == 1:
        return s
    step = len(s) // 3
    one = s[:step]
    two = s[step:2*step]
    three = s[2*step:]

    two = two.replace('-', ' ')
    
    return cantor_set(one) + cantor_set(two) + cantor_set(three)

while True:
    try:
        n = int(input())
        s = make_str(n)
        print(cantor_set(s))
    except:
        break