import sys

while 1:
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if not a[0] and not a[1]:
        break
    factor = a[1] % a[0]
    multiple = a[0] % a[1]
    if not factor and multiple:
        print("factor")
    elif factor and not multiple:
        print("multiple")
    elif factor and multiple:
        print("neither")