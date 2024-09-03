import sys
from itertools import combinations
nm = list(map(int,sys.stdin.readline().strip().split()))
card = list(map(int,sys.stdin.readline().strip().split()))
three_card = list(combinations(card, 3))

sum_card = []
for each_card in three_card:
    sum_card.append(sum(each_card))

min_gap = 100000
answer = 0
for i in sum_card:
    if i <= nm[1]:
        gap = nm[1] - i
        if min_gap > gap:
            min_gap = gap
            answer = i
print(answer)
   